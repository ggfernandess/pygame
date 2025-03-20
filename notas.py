import pygame as pg

pg.init()

largura_tela = 750
altura_tela = 750

tela = pg.display.set_mode((largura_tela, altura_tela))
pg.display.set_caption('Notas musicais')

do = pg.mixer.Sound('sons/do.wav')
re = pg.mixer.Sound('sons/re.wav')
mi = pg.mixer.Sound('sons/mi.wav')
fa = pg.mixer.Sound('sons/fa.wav')
so = pg.mixer.Sound('sons/sol.wav')
la = pg.mixer.Sound('sons/la.wav')
si = pg.mixer.Sound('sons/si.wav')

sons = {
    0: do,
    1: re,
    2: mi,
    3: fa,
    4: so,
    5: la,
    6: si
}

teclas = {
    pg.K_1: 0,
    pg.K_2: 1,
    pg.K_3: 2,
    pg.K_4: 3,
    pg.K_5: 4,
    pg.K_6: 5,
    pg.K_7: 6
}

cores = [
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 0),
    (255, 165, 0),
    (255, 0, 255),
    (0, 255, 255)
]

cores_ativadas = [
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255),
    (255, 255, 255)
]

nomes = ['Dó', 'Ré', 'Mi', 'Fá', 'Sol', 'Lá', 'Si']

fonte = pg.font.Font(None, 50)

run = True
cores_temp = cores.copy()
tempo_mudanca_cor = 300
tempo_ultimo_evento = None

while run:
    tela.fill((0, 0, 0))

    for i, (cor, nome) in enumerate(zip(cores_temp, nomes)):
        pg.draw.rect(tela, cor, (i * (largura_tela // 7), 0, largura_tela // 7, altura_tela))

        texto = fonte.render(nome, True, (255, 255, 255))
        texto_rect = texto.get_rect(center=(i * (largura_tela // 7) + largura_tela // 14, altura_tela // 2))
        tela.blit(texto, texto_rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            
            for i in range(7):
                if i * (largura_tela // 7) <= mouse_x < (i + 1) * (largura_tela // 7):
                    if 0 <= mouse_y <= altura_tela:
                        sons[i].play()
                        cores_temp[i] = cores_ativadas[i]
                        tempo_ultimo_evento = pg.time.get_ticks()

        elif event.type == pg.KEYDOWN:
            if event.key in teclas:
                sons[teclas[event.key]].play()
                index = teclas[event.key]
                cores_temp[index] = cores_ativadas[index]
                tempo_ultimo_evento = pg.time.get_ticks()

    if tempo_ultimo_evento:
        tempo_atual = pg.time.get_ticks()
        if tempo_atual - tempo_ultimo_evento > tempo_mudanca_cor:
            cores_temp = cores.copy()

    pg.display.update()

pg.quit()
