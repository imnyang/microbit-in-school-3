ㅁ = 0

def on_forever():
    global ㅁ
    basic.show_arrow(ㅁ)
    basic.clear_screen()
    ㅁ += 1
    if ㅁ == 7:
        ㅁ = 0
basic.forever(on_forever)
