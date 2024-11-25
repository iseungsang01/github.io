import pygame
import os
import time
import threading
from supabase import create_client, Client

player_name = str(input("Enter player_name : "))

note_data = []
title = ""
genre = ""
artist = ""
bpm = ""
key = ""
difficulty = ""
maker = ""
all_note = 0
oneNscore = 0.0

song_name = "FREEDOM_DiVE"

result = [0,0,0,0]
#perfect great bad miss
earlylate = [0,0]
#early late


dpush = 0
fpush = 0
jpush = 0
kpush = 0

speed = 20
score = 0.0
sudden = 0
sud = 0
scroll_count = 0

test_data = 0
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

BLACK = (00,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

FPS = 60

pygame.init()
pygame.mixer.init()
pygame.font.init()  # 폰트 모듈 초기화

#경로 지정
current_path = os.path.dirname(__file__)
assets_path =  os.path.join(current_path, "assets")
songs_path = os.path.join(current_path, "songs")

#이미지 경로 지정
#기어
gear_skin = pygame.image.load(os.path.join(assets_path, "gear_skin.png"))
key_beam = pygame.image.load(os.path.join(assets_path, "key_beam.png"))
gear_key_clicked_1 = pygame.image.load(os.path.join(assets_path, "gear_key_clicked_1.png"))
gear_key_unclicked_1 = pygame.image.load(os.path.join(assets_path, "gear_key_unclicked_1.png"))
gear_key_clicked_2 = pygame.image.load(os.path.join(assets_path, "gear_key_clicked_2.png"))
gear_key_unclicked_2 = pygame.image.load(os.path.join(assets_path, "gear_key_unclicked_2.png"))
inputline = pygame.image.load(os.path.join(assets_path, "input.png"))
gear_background = pygame.image.load(os.path.join(assets_path, "gear_background.png"))
#서든
sudden_img = pygame.image.load(os.path.join(assets_path, "sudden.png"))
#노트
note_image1 = pygame.image.load(os.path.join(assets_path, "note1.png"))
note_image2 = pygame.image.load(os.path.join(assets_path, "note2.png"))
test_note = pygame.image.load(os.path.join(assets_path, "test_note.png"))
#판정
perfect = pygame.image.load(os.path.join(assets_path, "perfect.png"))
great = pygame.image.load(os.path.join(assets_path, "great.png"))
bad = pygame.image.load(os.path.join(assets_path, "bad.png"))
miss = pygame.image.load(os.path.join(assets_path, "miss.png"))
#early, late
early_image = pygame.image.load(os.path.join(assets_path, "fast.png"))
late_image = pygame.image.load(os.path.join(assets_path, "slow.png"))
#song
song = 0

def count_zeros(matrix):
    count = 0
    for row in matrix:
        for element in row:
            if element == "0":
                count += 1
    return count


#체보파일, 곡 데이터 불러오기
def bring_data(name):
    """악곡 파일(.txt)를 노트파일과 곡 정보로 나누어서 정리해줍니다."""

    global title, genre, artist, bpm, difficulty, maker, bga, key, note_data, all_note, oneNscore, song
    경로 = os.path.dirname(os.path.realpath(__file__))
    f = open(경로 + """\songs\\""" + str(name)+"\\note.txt","r",encoding="UTF-8")
    song_D = f.read().split("\n")
    f.close()

    song = pygame.mixer.Sound(os.path.join(songs_path, name, "song.mp3"))

    song_data = song_D[0:10:1]
    note_data = song_D[10::1]

    all_note = count_zeros(note_data)
    oneNscore = 1000000/all_note

    title = song_data[1].split(" ")[1]
    genre = song_data[2].split(" ")[1]
    artist = song_data[3].split(" ")[1]
    bpm = song_data[4].split(" ")[1]
    difficulty = song_data[5].split(" ")[1]
    maker = song_data[6].split(" ")[1]
    bga = song_data[7].split(" ")[1]
    key = song_data[8].split(" ")[1]

    title = title.replace("_"," ")
    genre = genre.replace("_"," ")
    artist = artist.replace("_"," ")
    difficulty = difficulty.replace("_"," ")
    maker = maker.replace("_"," ")
    bga = bga.replace("_"," ")
    key = key.replace("_"," ")

    title = title.replace("\-","_")
    genre = genre.replace("\-","_")
    artist = artist.replace("\-","_")
    difficulty = difficulty.replace("\-","_")
    maker = maker.replace("\-","_")
    bga = bga.replace("\-","_")
    key = key.replace("\-","_")

bring_data(song_name)

#위에 가림막
def suddenplus():
    global sud, sudden
    if sudden != 800:
        if sud == 1:
            sudden += 1
        elif sud == -1:
            sudden += -1
    
    if sudden == -1:
        sudden == 0
    screen.blit(sudden_img,[SCREEN_WIDTH//2 - 300, -800 + sudden])

#기어 아래 누르면 들어가는 이미지 출력하는 코드
def gear_switch():
    if dpush == 1:
        #1번 라인
        screen.blit(gear_key_clicked_1,[SCREEN_WIDTH//2 - 500 + 200,1080-280])
    else:
        screen.blit(gear_key_unclicked_1,[SCREEN_WIDTH//2 - 500 + 200,1080-280])
    if fpush == 1:
        #2번 라인
        screen.blit(gear_key_clicked_2,[SCREEN_WIDTH//2 - 500 + 350,1080-280])
    else:
        screen.blit(gear_key_unclicked_2,[SCREEN_WIDTH//2 - 500 + 350,1080-280])
    if jpush == 1:
        #3번 라인
        screen.blit(gear_key_clicked_2,[SCREEN_WIDTH//2 - 500 + 500,1080-280])
    else:
        screen.blit(gear_key_unclicked_2,[SCREEN_WIDTH//2 - 500 + 500,1080-280])

    if kpush == 1:
        #4번 라인
        screen.blit(gear_key_clicked_1,[SCREEN_WIDTH//2 - 500 + 650,1080-280])
    else:
        screen.blit(gear_key_unclicked_1,[SCREEN_WIDTH//2 - 500 + 650,1080-280])

def print_key_beam():
    if dpush == 1:
        screen.blit(key_beam, [SCREEN_WIDTH//2 - 500 + 200, 0])

    if fpush == 1:
        screen.blit(key_beam,[SCREEN_WIDTH//2 - 500 + 350, 0])

    if jpush == 1:
        screen.blit(key_beam,[SCREEN_WIDTH//2 - 500 + 500, 0])

    if kpush == 1:
        screen.blit(key_beam,[SCREEN_WIDTH//2 - 500 + 650, 0])

song_play = 0

#소리 경로 지정
hit_sound = pygame.mixer.Sound(os.path.join(assets_path, "hitsound.wav"))

pygame.display.set_caption("RHYTHM GAME")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

clock = pygame.time.Clock()

Running = True

class Note:
    def __init__(self, speed, note1, note2):
        self.pscreen = [['-' for j in range(4)] for i in range(270)]
        self.speed = speed
        self.image1 = note1
        self.image2 = note2
        self.testdata = 0
        self.score = [0,0,0,0]
        self.earlylate = ""
        self.puc = ""
        self.pscore = 0
        self.last_print = ["",""]

    def scroll(self):
        global test_data, song_play
        # 스크롤을 위해 현재 화면을 한 줄씩 아래로 이동
        for i in range(len(self.pscreen) - 1, 0, -1):
            self.pscreen[i] = self.pscreen[i - 1]  # 깊은 복사
        song_play += 1
        # 스크롤에 따른 위치 계산 및 이미지 출력
        for j in range(len(self.pscreen)):  # pscreen의 길이만큼 반복
            # j가 pscreen의 범위 내에 있는지 확인
            if j < len(self.pscreen):
                if str(self.pscreen[j][0]) == "0":
                    screen.blit(self.image1, (SCREEN_WIDTH // 2 - 300, j * self.speed * 4 - 700 * (self.speed - 1) - 75))
                if str(self.pscreen[j][1]) == "0":
                    screen.blit(self.image2, (SCREEN_WIDTH // 2 - 150, j * self.speed * 4 - 700 * (self.speed - 1) - 75))
                if str(self.pscreen[j][2]) == "0":
                    screen.blit(self.image2, (SCREEN_WIDTH // 2 + 0, j * self.speed * 4 - 700 * (self.speed - 1) - 75))
                if str(self.pscreen[j][3]) == "0":
                    screen.blit(self.image1, (SCREEN_WIDTH // 2 + 150, j * self.speed * 4 - 700 * (self.speed - 1) - 75))
        if song_play == 130:
            song.play()
    def summon_note(self, note):
        self.pscreen[0] = note  # 새 노트를 화면의 첫 번째 행에 추가

    def KB_input(self, lane):
        global score, oneNscore, result, earlylate
        # 높은 판정부터 순서대로 조건을 확인하여 중복되지 않게 처리
        for i in range(175, 181):  # Perfect 판정 구간
            if self.pscreen[i][lane] == "0":
                self.pscreen[i][lane] = "-"
                self.last_print = ["perfect", ""]
                score += oneNscore
                result[0] += 1
                self.pscore = 0  # 새로운 입력이 발생했을 때 pscore를 초기화
                return  # 한 번 판정되면 바로 함수 종료

        for i in range(173, 175):  # Great (early) 판정 구간
            if self.pscreen[i][lane] == "0":
                self.pscreen[i][lane] = "-"
                self.last_print = ["great", "early"]
                score += (oneNscore/4)*3
                result[1] += 1
                earlylate[0] += 1
                self.pscore = 0
                return

        for i in range(181, 183):  # Great (late) 판정 구간
            if self.pscreen[i][lane] == "0":
                self.pscreen[i][lane] = "-"
                self.last_print = ["great", "late"]
                score += (oneNscore/4)*3
                result[1] += 1
                earlylate[1] += 1
                self.pscore = 0
                return

        for i in range(171, 173):  # Bad (early) 판정 구간
            if self.pscreen[i][lane] == "0":
                self.pscreen[i][lane] = "-"
                self.last_print = ["bad", "early"]
                score += oneNscore/4
                result[2] += 1
                earlylate[0] += 1
                self.pscore = 0
                return

        for i in range(183, 185):  # Bad (late) 판정 구간
            if self.pscreen[i][lane] == "0":
                self.pscreen[i][lane] = "-"
                self.last_print = ["bad", "late"]
                score += oneNscore/4
                result[2] += 1
                earlylate[1] += 1
                self.pscore = 0
                return

    def end_game(self):
        global Running
        if self.pscreen[180][0] == "e":
            Running = False
            return  # 한 번 판정되면 바로 함수 종료

    def miss_del(self, lane):
        if self.pscreen[186][lane] == "0":
            self.pscreen[186][lane] = "-"
            self.last_print = ["miss",""]
            result[3] += 1
            self.pscore = 0
            return
            
    def print_note(self):
        # last_print가 빈 상태가 아닐 때만 판정 이미지 출력
        if self.last_print[0] != "":
            self.pscore += 1
            if self.last_print[0] == "perfect":
                screen.blit(perfect, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2])
            elif self.last_print[0] == "great":
                screen.blit(great, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2])
            elif self.last_print[0] == "bad":
                screen.blit(bad, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2])
            elif self.last_print[0] == "miss":
                screen.blit(miss, [SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2])

            if self.last_print[1] == "early":
                screen.blit(early_image, [SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100])
            elif self.last_print[1] == "late":
                screen.blit(late_image, [SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 + 100])

        # 일정 시간이 지난 후 초기화하여 판정 이미지가 유지되지 않도록 함
        if self.pscore >= 15:
            self.pscore = 0
            self.last_print = ["", ""]

def print_song(scroll):
    note_data_entry = list(note_data[scroll][:4])  # 첫 네 요소를 리스트로 가져옴
    note.summon_note(note_data_entry)

def play_song():
    global scroll_count
    interval = (3.75*3)/float(bpm)   # 초 단위의 간격
    next_time = time.time()

    while True:
        if scroll_count < len(note_data):  # note_data의 범위 내에서 접근하는지 확인
            if len(note_data[scroll_count]) == 4:
                print_song(scroll_count)
                scroll_count += 1
            else:
                note.summon_note(["-", "-", "-", "-"])
            scroll_count += 1
        else:
            # 만약 scroll_count가 note_data의 길이보다 크다면 루프를 종료하거나 대기 상태로 유지합니다.
            break

        next_time += interval
        sleep_time = max(0, next_time - time.time())
        time.sleep(sleep_time)

note = Note(speed, note_image1, note_image2)

def game():
    global score, dpush, fpush, jpush, kpush, Running, sud
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                dpush = 1
                hit_sound.play()
                note.KB_input(0)
            elif event.key == pygame.K_f:
                fpush = 1
                hit_sound.play()
                note.KB_input(1)
            elif event.key == pygame.K_j:
                jpush = 1
                hit_sound.play()
                note.KB_input(2)
            elif event.key == pygame.K_k:
                kpush = 1
                hit_sound.play()
                note.KB_input(3)
            elif event.key == pygame.K_ESCAPE:
                Running = False
            elif event.key == pygame.K_UP:
                sud = -1
            elif event.key == pygame.K_DOWN:
                sud = 1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                dpush = 0
            elif event.key == pygame.K_f:
                fpush = 0
            elif event.key == pygame.K_j:
                jpush = 0
            elif event.key == pygame.K_k:
                kpush = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                sud = 0

    note.miss_del(0)
    note.miss_del(1)
    note.miss_del(2)
    note.miss_del(3)

    screen.fill(BLACK)

    screen.blit(gear_background,[SCREEN_WIDTH//2 - 300 ,0])

    note.end_game()


    font = pygame.font.SysFont("UDGOTHICR", 35)

    print_score = str(int(score))
    print_score = print_score.zfill(7)
    text = font.render(print_score, True, WHITE)


    print_key_beam()
    note.scroll()

    screen.blit(inputline,[SCREEN_WIDTH//2 - 500 + 200, 1080 - 280 - 100])
    screen.blit(gear_skin,[SCREEN_WIDTH//2 - 500 ,0])
    screen.blit(text, [920, 1000])
    suddenplus()
    gear_switch()
    note.print_note()

    pygame.display.flip()
    clock.tick(FPS)

def game_roof():
    while Running == True:
        game()

# Supabase 초기화
def initialize_supabase():
    url = "https://jaxoyvpxrrwgqixcakag.supabase.co/"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImpheG95dnB4cnJ3Z3FpeGNha2FnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzAxOTM0NzcsImV4cCI6MjA0NTc2OTQ3N30.Z8wyBD_5HGu8Hu5PErbVRlIrjWMZzi8-4IrnQVYPyoM"
    return create_client(url, key)

supabase = initialize_supabase()

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




thread = threading.Thread(target=play_song)
thread.daemon = True

thread.start()

game_roof()

song.stop()

upload_data(player_name, score)

if __name__ == "__main__":
    main()

pygame.quit()