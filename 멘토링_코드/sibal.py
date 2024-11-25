import pygame
import os
import random

# Pygame 초기화
pygame.init()
pygame.mixer.init()

# 화면 크기 설정
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("리듬 게임")

# 색상 정의
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 프레임 속도 설정
FPS = 60
clock = pygame.time.Clock()

# 노트 속도
note_speed = 1

# 이미지 및 사운드 경로
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, "assets")

# 이미지 로드
gear_skin = pygame.image.load(os.path.join(assets_path, "gear_skin.png"))
note_image = pygame.image.load(os.path.join(assets_path, "note1.png"))
hit_sound = pygame.mixer.Sound(os.path.join(assets_path, "hitsound.wav"))

# 점수 표시를 위한 폰트
font = pygame.font.SysFont("Arial", 30, True, False)

# 게임 전역 변수
score = 0
note_list = []
running = True

# 노트 클래스
class Note:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed
        self.image = note_image
        self.hit_zone = SCREEN_HEIGHT - 100  # 판정 영역

    def update(self):
        self.y += self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def is_hit(self, key_input):
        """노트가 판정 영역에 들어왔을 때 키 입력을 받으면 성공"""
        if self.y >= self.hit_zone - 10 and self.y <= self.hit_zone + 10:
            if key_input:
                hit_sound.play()
                return True
        return False

# 노트 생성 함수
def generate_notes():
    positions = [200, 300, 400, 500]  # 각 노트가 나타날 x좌표 (각 키에 대응)
    key_binds = [pygame.K_d, pygame.K_f, pygame.K_j, pygame.K_k]  # 각 키와 노트 매핑
    note = Note(random.choice(positions), note_speed)
    note_list.append((note, random.choice(key_binds)))

# 게임 종료 함수
def game_over():
    global running
    running = False

# 메인 게임 루프
def main_game():
    global score, running, note_list

    # 일정 시간마다 노트 생성
    pygame.time.set_timer(pygame.USEREVENT, 1500)

    while running:
        screen.fill(BLACK)  # 배경 색상

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()
            elif event.type == pygame.USEREVENT:
                generate_notes()  # 주기적으로 노트 생성

        # 키 입력 처리
        keys = pygame.key.get_pressed()

        # 노트 갱신 및 판정
        for note, key in note_list[:]:
            note.update()
            note.draw()

            # 노트가 판정 영역에 도달했을 때 키가 눌렸는지 확인
            if note.is_hit(keys[key]):
                score += 100  # 성공 시 점수 추가
                note_list.remove((note, key))  # 성공한 노트는 리스트에서 제거

            # 노트가 화면을 벗어나면 제거
            elif note.y > SCREEN_HEIGHT:
                note_list.remove((note, key))

        # 점수 출력
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()  # 화면 업데이트
        clock.tick(FPS)

    pygame.quit()

# 게임 시작
main_game()
