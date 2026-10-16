"""Gera figuras didáticas a partir das dimensões nominais do exercício 07."""
from pathlib import Path
import os
import tempfile

os.environ.setdefault('MPLCONFIGDIR', str(Path(tempfile.gettempdir()) / 'dac_mpl'))
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

OUT = Path(__file__).resolve().parent
INK, BLUE, GRAY = '#203244', '#176d9c', '#dceaf2'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                     'text.color': INK, 'axes.titlecolor': INK})


def setup(ax, title, xlim, ylim):
    ax.set_aspect('equal')
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis('off')
    ax.set_title(title, fontweight='bold', pad=16)


def rect(ax, x, y, w, h, **kw):
    ax.add_patch(Rectangle((x, y), w, h, edgecolor=INK, linewidth=1.5,
                           facecolor=kw.pop('facecolor', GRAY), **kw))


def dim(ax, a, b, off, label, vertical=False):
    if vertical:
        x, ya = a; _, yb = b
        ax.plot([x, off], [ya, ya], color=BLUE, lw=.6)
        ax.plot([x, off], [yb, yb], color=BLUE, lw=.6)
        ax.annotate('', (off, ya), (off, yb),
                    arrowprops={'arrowstyle': '<->', 'color': BLUE, 'lw': .9})
        ax.text(off-2, (ya+yb)/2, label, rotation=90, ha='right', va='center', color=BLUE)
    else:
        xa, y = a; xb, _ = b
        ax.plot([xa, xa], [y, off], color=BLUE, lw=.6)
        ax.plot([xb, xb], [y, off], color=BLUE, lw=.6)
        ax.annotate('', (xa, off), (xb, off),
                    arrowprops={'arrowstyle': '<->', 'color': BLUE, 'lw': .9})
        ax.text((xa+xb)/2, off+1.6, label, ha='center', va='bottom', color=BLUE)


def leader(ax, text, xy, xytext):
    ax.annotate(text, xy, xytext, color=BLUE, fontsize=10,
                arrowprops={'arrowstyle': '->', 'color': BLUE, 'lw': 1},
                ha='left', va='center')


def front(ax, hole=True, hidden=True):
    rect(ax, 0, 0, 100, 10)
    rect(ax, 30, 10, 40, 30)
    if hole:
        ax.add_patch(Circle((50, 25), 8, facecolor='white', edgecolor=INK, lw=1.5))
        ax.plot([38, 62], [25, 25], '-.', color=BLUE, lw=.7)
        ax.plot([50, 50], [13, 37], '-.', color=BLUE, lw=.7)
    if hidden:
        for x in [8, 16, 84, 92]:
            ax.plot([x, x], [0, 10], '--', color=INK, lw=.8)


def save(fig, name, note):
    fig.text(.5, .025, note, ha='center', fontsize=10, color=INK)
    fig.savefig(OUT / name, dpi=180, facecolor='white')
    plt.close(fig)


# Vistas separadas para estudo: a disposição não define um sistema de projeção.
fig, (top, fr) = plt.subplots(2, 1, figsize=(11, 12))
fig.subplots_adjust(hspace=.28, bottom=.08, top=.88)
fig.suptitle('ATIVIDADE 07 • Suporte para fixação de tubo', fontsize=18, fontweight='bold')
setup(top, 'Vista superior — posição dos furos e do ressalto', (-22, 150), (-23, 85))
rect(top, 0, 0, 100, 60)
rect(top, 30, 15, 40, 30, facecolor='#b9d6e8')
for x in [12, 88]:
    for y in [12, 48]:
        top.add_patch(Circle((x, y), 4, facecolor='white', edgecolor=INK, lw=1.3))
        top.plot([x-6, x+6], [y, y], '-.', color=BLUE, lw=.6)
        top.plot([x, x], [y-6, y+6], '-.', color=BLUE, lw=.6)
for x in [42, 58]:
    top.plot([x, x], [15, 45], '--', color=INK, lw=.8)
top.add_patch(Circle((50, 30), 3.3, facecolor='white', edgecolor=INK, lw=1.2))
top.add_patch(Circle((50, 30), 4, fill=False, edgecolor=BLUE, lw=.8))
top.plot([50, 50], [10, 50], '-.', color=BLUE, lw=.7)
dim(top, (0, 60), (100, 60), 74, '100')
dim(top, (0, 0), (0, 60), -13, '60', True)
dim(top, (30, 15), (70, 15), -16, '40 — ressalto centralizado')
dim(top, (100, 12), (100, 48), 111, '36', True)
dim(top, (12, 48), (88, 48), 65, '76 entre centros')
dim(top, (0, 0), (12, 0), -7, '12')
dim(top, (100, 0), (100, 12), 103, '12', True)
dim(top, (70, 15), (70, 45), 78, '30', True)
leader(top, 'M8 no centro\ndo ressalto', (53, 31), (119, 24))
leader(top, '4 × Ø8\nPASSANTES', (91, 50), (108, 55))

setup(fr, 'Vista frontal — olhando na direção do furo Ø16', (-22, 135), (-17, 65))
front(fr)
fr.plot([46, 46], [32, 40], '--', color=INK, lw=.8)
fr.plot([54, 54], [32, 40], '--', color=INK, lw=.8)
dim(fr, (0, 0), (100, 0), -10, '100')
dim(fr, (30, 40), (70, 40), 52, '40')
dim(fr, (0, 0), (0, 10), -9, '10', True)
dim(fr, (30, 0), (30, 25), -17, '25 desde a face inferior', True)
dim(fr, (70, 0), (70, 40), 112, '40 — altura total', True)
leader(fr, 'Ø16 PASSANTE\nna direção dos 30 mm', (56, 29), (77, 57))
save(fig, '01_vistas_cotadas.png', 'Dimensões em mm • Contornos nominais, antes dos chanfros • Vistas de estudo; sem escala de impressão')

# Corte longitudinal em X = 50: a rosca é representada de forma simplificada.
fig, ax = plt.subplots(figsize=(12, 7))
fig.subplots_adjust(bottom=.13, top=.88)
setup(ax, 'Corte didático pelo centro • plano X = 50', (-25, 130), (-12, 65))
rect(ax, 0, 0, 60, 10, hatch='///')
rect(ax, 15, 10, 30, 30, hatch='///')
rect(ax, 15, 17, 30, 16, facecolor='white')
# A abertura vertical atravessa apenas a parede superior do furo horizontal.
rect(ax, 26, 33, 8, 7, facecolor='white')
ax.plot([26.1, 33.9], [33, 33], color='white', lw=2.5)
ax.plot([30, 30], [14, 47], '-.', color=BLUE, lw=.8)
ax.plot([10, 50], [25, 25], '-.', color=BLUE, lw=.8)
ax.plot([26, 34], [30, 30], '--', color=BLUE, lw=.8)
dim(ax, (15, 10), (45, 10), -6, '30 — comprimento atravessado pelo Ø16')
dim(ax, (15, 17), (15, 33), -8, 'Ø16', True)
dim(ax, (45, 0), (45, 25), 64, '25', True)
dim(ax, (15, 33), (15, 40), -18, '7', True)
dim(ax, (34, 30), (34, 40), 77, '10 — extensão nominal', True)
leader(ax, 'M8 vertical\nRosca simplificada', (33, 37), (57, 53))
leader(ax, 'Comunicação\nentre os furos', (30, 33), (84, 44))
leader(ax, 'Fim nominal em Z = 30\n(dentro do vazio)', (33, 30), (82, 17))
ax.text(18, 21, 'Vazio do furo Ø16', color=BLUE, fontsize=10)
save(fig, '02_corte_comunicacao.png', 'Esquema de interpretação • Hachura = material • Rosca e ponta de broca sem detalhamento • Dimensões em mm')

fig, axs = plt.subplots(2, 2, figsize=(12, 9))
fig.subplots_adjust(hspace=.4, wspace=.2, top=.88, bottom=.12)
fig.suptitle('Sequência de modelagem • leitura pela vista frontal', fontsize=17, fontweight='bold')
titles = ['1. Base: extrusão de 10 mm', '2. Ressalto: adicionar 30 mm',
          '3. Quatro furos Ø8 + furo horizontal Ø16', '4. M8 superior + chanfros finais']
for i, (ax, title) in enumerate(zip(axs.flat, titles)):
    setup(ax, title, (-8, 108), (-8, 60))
    if i == 0:
        rect(ax, 0, 0, 100, 10)
        dim(ax, (0, 10), (100, 10), 28, '100 × 60 em planta')
    else:
        front(ax, hole=i >= 2, hidden=i >= 2)
    if i == 1:
        ax.text(50, 49, '40 × 30 em planta; centralizado', ha='center', color=BLUE)
    if i == 2:
        ax.text(50, 51, 'Padrão 2 × 2: 76 mm × 36 mm', ha='center', color=BLUE)
    if i == 3:
        ax.plot([46, 46], [32, 40], '--', color=BLUE, lw=1.1)
        ax.plot([54, 54], [32, 40], '--', color=BLUE, lw=1.1)
        ax.text(50, 51, 'M8 no topo: profundidade nominal 10', ha='center', color=BLUE)
        ax.plot([1, 29], [10, 10], color='#df7b22', lw=3)
        ax.plot([71, 99], [10, 10], color='#df7b22', lw=3)
        ax.text(50, -6, 'Laranja: perímetro superior externo da base', ha='center', fontsize=9, color='#a6500a')
save(fig, '03_sequencia_modelagem.png', 'Esquemas de construção • Arestas ocultas tracejadas • Chanfros de 1 × 45° aplicados ao final')

print('Geradas 3 ilustrações em', OUT)
