집가고싶다 = 0
집안가고싶다 = -1
def on_forever():
    global 집가고싶다
    global 집안가고싶다
    basic.show_arrow(집가고싶다)
    basic.clear_screen()
    basic.pause(500)
    집가고싶다 += 1
    if 집가고싶다 == 7:
        집가고싶다 = 0
    else:
        집안가고싶다 -= 1
        

basic.forever(on_forever)
