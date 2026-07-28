import cv2
import json

def load_event_data(json_filepath):
    """讀取 JSON 檔案，只保留 '發球' 和 '動作' 事件"""

    print(f"嘗試讀取檔案: {json_filepath}...")

    try:
        with open(json_filepath, "r", encoding="utf-8") as f:
            json_data = json.load(f)

        if "events" not in json_data:
            print("錯誤：JSON 中沒有 'events' 欄位。")
            return None

        EVENTS_TO_KEEP = {"發球", "動作"}

        event_data = [
            event
            for event in json_data["events"]
            if event.get("eventType") in EVENTS_TO_KEEP
        ]

        print(f"成功讀取 {len(json_data['events'])} 筆原始事件資料。")
        print(f"過濾後保留 {len(event_data)} 筆 '發球' 和 '動作' 事件。")

        return event_data

    except FileNotFoundError:
        print(f"錯誤：找不到檔案 {json_filepath}")
        return None

    except json.JSONDecodeError as e:
        print(f"JSON 格式錯誤：{e}")
        return None

    except Exception as e:
        print(f"讀取 JSON 檔案時發生錯誤：{e}")
        return None

def group_events_by_rally(data):
    """將所有事件依 '發球' 分組，形成多個回合 (Rallies)"""
    rallies = []
    current_rally = []
    
    data.sort(key=lambda x: x.get('index', x.get('startFrame', 0))) 
    
    for event in data:
        is_serve = (event.get('eventType') == '發球')
        
        if is_serve and current_rally:
            rallies.append(current_rally)
            current_rally = [event]
        else:
            current_rally.append(event)
            
    if current_rally:
        rallies.append(current_rally)
        
    if rallies and rallies[0] and rallies[0][0].get('eventType') != '發球':
        rallies.pop(0)

    for i, rally in enumerate(rallies):
        serve = rally[0]
        print(
            f"Rally {i+1}",
            "index =", serve["index"],
            "frame =", serve["startFrame"]
        )
            
    return rallies

def get_forehand_backhand(event):
    """從事件的 labels 中提取 '正/反拍' 資訊"""
    labels = event.get('labels', [])
    event_type = event.get('eventType')
    
    if event_type == '發球':
        target_name = '正反手'
    elif event_type == '動作':
        target_name = '擊球拍面'
    else:
        return 'N/A'
    
    for label in labels:
        if label.get('name') == target_name:
            return label.get('value', 'N/A')
            
    return 'N/A'

def get_action_type(event):
    """從事件的 labels 中提取具體的 '動作類型' 資訊"""
    event_type = event.get('eventType')
    
    if event_type == '發球':
        # 發球事件，動作類型直接標註為 '發球'
        return '發球' 
    elif event_type == '動作':
        labels = event.get('labels', [])
        for label in labels:
            # 查找 name 為 '動作' (且 type 也是 '動作') 的標籤
            if label.get('name') == '動作' and label.get('type') == '動作':
                return label.get('value', 'N/A')
    return 'N/A'

def mark_and_process_rallies(video_path, event_data, output_filepath):
    """處理影片，等待發球標記，並自動交替標記同一回合中後續的事件"""
    
    rallies = group_events_by_rally(event_data)
    if not rallies:
        print("錯誤：未在提供的資料中找到任何包含 '發球' 的回合。")
        return

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"錯誤：無法開啟影片檔案 {video_path}。請確認路徑是否正確。")
        return

    final_marked_events = []
    
    print(f"總共找到 {len(rallies)} 個回合需要標記。")
    print("\n--- 開始發球動作標記 ---")
    print("操作： [z] 左選手 | [x] 右選手 | [a] 幀退 | [d] 幀進 | [q] 退出並儲存")
    
    cv2.namedWindow('Table Tennis Auto Marker (桌球自動標記工具)')

    try:
        for i, rally in enumerate(rallies):
            serve_event = rally[0]
            start_frame = serve_event.get('startFrame')
            duration = serve_event.get('duration')
            end_frame = start_frame + duration
            
            current_frame = start_frame 
            serve_player = None

            while True: 
                cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
                ret, frame = cap.read()

                if not ret:
                    print(f"警告：無法讀取幀數 {current_frame}，跳過此回合。")
                    break 

                display_text_1 = f"Rally {i+1}/{len(rallies)} | Serve Frame: {start_frame} | Current Frame: {current_frame}"
                display_text_2 = f" [z] Left | [x] Right | [a] Back | [d] Forward | [e] End | [q] Quit"
                
                # Use cv2.putText for English/non-Chinese text (faster and no need for PIL setup)
                cv2.putText(frame, display_text_1, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, display_text_2, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, cv2.LINE_AA)
                
                cv2.imshow('Table Tennis Auto Marker (桌球自動標記工具)', frame)

                key = cv2.waitKey(0) & 0xFF
                
                # 處理幀檢視按鍵
                if key == KEY_A:
                    if current_frame > start_frame:
                        current_frame -= 1
                    else:
                        pass
                elif key == KEY_D:
                    if current_frame < end_frame:
                        current_frame += 1
                    else:
                        pass
                elif key == KEY_E:
                    current_frame = end_frame
                
                # 處理選擇/退出按鍵
                elif key == KEY_Z:
                    serve_player = 'L'
                    next_player = 'R'
                    break
                elif key == KEY_X:
                    serve_player = 'R'
                    next_player = 'L'
                    break
                elif key == KEY_Q:
                    serve_player = None
                    break
                else:
                    print(f"請按 [z], [x], [q] 進行選擇，或按 [a], [d] 進行幀查看。")

            if serve_player is None:
                if key == KEY_Q:
                    break 
                else:
                    break 

            
            current_player = serve_player
            
            for event_index, event in enumerate(rally):
                if event_index == 0:
                    event_player = serve_player
                    current_player = next_player
                else:
                    event_player = current_player
                    current_player = 'R' if current_player == 'L' else 'L' 

                fb_type = get_forehand_backhand(event)
                action_type = get_action_type(event) 
                
                marked_event = {
                    "player": event_player,
                    "eventType": event.get('eventType'),
                    "F_B_Type": fb_type, 
                    "Action_Type": action_type, # 紀錄動作類型
                    "startFrame": event.get('startFrame'),
                    "duration": event.get('duration'),
                    "index": event.get('index') 
                }
                final_marked_events.append(marked_event)
            
            print(f"已紀錄回合 {i+1} ({serve_player} 發球)，包含 {len(rally)} 個事件。")

    finally:
        cap.release()
        cv2.destroyAllWindows()

    if final_marked_events:
        print(f"\n--- 正在寫入結果到檔案: {output_filepath} ---")
        try:
            with open(output_filepath, 'w', encoding='utf-8') as f:
                f.write(f"{'Player':<8} {'EventType':<8} {'正/反拍':<8} {'動作類型':<12} {'StartFrame':<12} {'Duration':<8} {'Index':<8}\n")
                f.write("-" * 75 + "\n")
                
                for event in final_marked_events:
                    line = (
                        f"{event['player']:<8} "
                        f"{event['eventType']:<8} "
                        f"{event['F_B_Type']:<8} " 
                        f"{event['Action_Type']:<12} " 
                        f"{event['startFrame']:<12} "
                        f"{event['duration']:<8} "
                        f"{event['index']:<8}\n"
                    )
                    f.write(line)
            print(f"成功將 {len(final_marked_events)} 個事件記錄到 {output_filepath}")
        except Exception as e:
            print(f"寫入檔案時發生錯誤: {e}")
    else:
        print("沒有完成任何標記，未生成輸出檔案。")


if __name__ == "__main__":
    KEY_Z = ord('z') # 左選手
    KEY_X = ord('x') # 右選手
    KEY_Q = ord('q') # 退出
    KEY_A = ord('a') # 上一個幀
    KEY_D = ord('d') # 下一個幀
    KEY_E = ord('e') # 跳到最後一個frame

    name = "65a7fSWxre" # 
    VIDEO_PATH = f"./YT_videos/{name}.mp4" 

    OUTPUT_DIR = 'label_txt'
    JSON_DIR = 'label_jsons'
    JSON_FILENAME = f"./YT_json/{name}_data_YT.json"

    OUTPUT_FILENAME = JSON_FILENAME.replace('.json', '.txt')
    OUTPUT_FILENAME = OUTPUT_FILENAME.replace("label_jsons", "label_txt")

    events = load_event_data(JSON_FILENAME)
    if events:
        mark_and_process_rallies(VIDEO_PATH, events, OUTPUT_FILENAME)
