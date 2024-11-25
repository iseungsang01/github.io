import pygame
import os
from supabase import create_client, Client

# Supabase 초기화
def initialize_supabase():
    url = "https://jaxoyvpxrrwgqixcakag.supabase.co/"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpheG95dnB4cnJ3Z3FpeGNha2FnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxOTM0NzcsImV4cCI6MjA0NTc2OTQ3N30.Z8wyBD_5HGu8Hu5PErbVRlIrjWMZzi8-4IrnQVYPyoM"
    return create_client(url, key)

supabase = initialize_supabase()

# 전역 변수 정의
note_data, display_zenichi = [], []
title, genre, artist, bpm, key, difficulty, maker = "", "", "", "", "", "", ""
all_note, oneNscore, song, score = 0, 0.0, None, 1100000
result = [998, 0, 0, 1]  # perfect, great, bad, miss
earlylate = [4, 4]  # early, late

# 폰트 초기화
def load_fonts():
    return pygame.font.SysFont("GULIM", 40), pygame.font.SysFont("GULIM", 140)

# 경로 설정
def get_asset_paths():
    current_path = os.path.dirname(__file__)
    assets_path = os.path.join(current_path, "assets")
    songs_path = os.path.join(current_path, "songs")
    return assets_path, songs_path

assets_path, songs_path = get_asset_paths()

# 상위 점수 가져오기 함수
def fetch_top_scores(cutter=10):
    response = []
    score_data = supabase.table("scores").select("*").order("score", desc=True).limit(cutter).execute()
    if score_data.data:
        for item in score_data.data:
            response.append([str(item["name"]), int(item["score"])])
    return response

# 점수 업로드 함수
def upload_data(name, score_input):
    try:
        score = int(score_input)
        data = {"name": name, "score": score}
        response = supabase.table("scores").insert(data).execute()
        return f"{name}의 점수 {score}가 성공적으로 저장되었습니다." if response.data else f"오류 발생: {response.error}"
    except ValueError:
        return "유효한 숫자를 입력하세요."

# UI 요소 초기화 함수
def initialize_UI_elements(screen, clock, font, score_font, score, zenichi, result, earlylate):
    """게임 UI 요소를 초기화하고 화면에 표시하는 함수"""
    
    # zenichi 리스트를 기반으로 상위 10개의 점수를 화면에 표시할 텍스트로 렌더링
    display_zenichi = []
    for data in zenichi:
        result_score = f"{data[1]}점 : {data[0]}"
        display_zenichi.append(font.render(result_score, True, BLACK))
    
    # 판정 결과 및 점수 결과 텍스트 렌더링
    result_print = [
        font.render(f"perfect : {result[0]}", True, GREEN),
        font.render(f"great : {result[1]}", True, BLUE),
        font.render(f"bad : {result[2]}", True, WHITE),
        font.render(f"miss : {result[3]}", True, RED)
    ]
    
    # Early, late 결과 텍스트 렌더링
    earlylate_print = [
        font.render(f"early : {earlylate[0]}", True, BLUE),
        font.render(f"late : {earlylate[1]}", True, RED)
    ]
    
    # 총 점수 렌더링
    print_score = score_font.render(f"Score: {int(score)}", True, WHITE)

    # UI 화면 출력 함수
    def end_UI():
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, pygame.Rect(20, 20, 600, 450))
        
        # 상위 10개 점수 표시
        for i, text_surface in enumerate(display_zenichi):
            screen.blit(text_surface, (100, 50 + i * 40))
        
        # 총 점수와 판정 결과 표시
        screen.blit(print_score, (screen.get_width() // 2 - 200, screen.get_height() // 2 - 300))
        for i, text in enumerate(result_print[::-1]):
            screen.blit(text, (screen.get_width() // 2 - 200, screen.get_height() // 2 - 35 - (i * 45)))
        for i, text in enumerate(earlylate_print):
            screen.blit(text, (screen.get_width() // 2 + 100, screen.get_height() // 2 - 40 - (i * 40)))
        
        pygame.display.flip()
        clock.tick(60)
    
    return end_UI

# 메인 게임 실행 함수
def main():
    pygame.init()  # pygame과 폰트 시스템 초기화
    pygame.font.init()  # 폰트 시스템 초기화
    
    # 화면과 시계 설정
    SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("RHYTHM GAME")
    clock = pygame.time.Clock()
    
    # 폰트 및 데이터 초기화
    font, score_font = load_fonts()  # 초기화 후 폰트를 불러옵니다.
    zenichi = fetch_top_scores(10)   # 상위 점수 10개 불러오기
    
    # UI 요소 초기화
    end_UI = initialize_UI_elements(screen, clock, font, score_font, score, zenichi, result, earlylate)
    
    # 게임 루프
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
        
        # UI 업데이트
        end_UI()
    
    pygame.quit()

if __name__ == "__main__":
    main()
