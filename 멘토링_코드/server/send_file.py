import requests

def end_game(score):
    """게임 종료 시 호출되는 함수"""
    url = 'http://127.0.0.1:5000/send_data'
    
    # POST 요청으로 하이스코어 전송
    response = requests.post(url, json={'score': score})
    
    if response.ok:
        data = response.json()
        print(f"New high score is: {data['new_high_score']}")
    else:
        print(f"Failed to send score: {response.status_code}")

# 게임 로직의 예
def play_game():
    # 게임 플레이 코드 (예: 점수 계산)
    score = 12  # 예시 점수
    print("Game Over!")
    
    # 게임 종료 시 하이스코어 전송
    end_game(score)

if __name__ == "__main__":
    play_game()
