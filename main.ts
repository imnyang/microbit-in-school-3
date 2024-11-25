let 집가고싶다 = 0

basic.forever(function () {
    basic.showArrow(집가고싶다)
    basic.clearScreen()
    basic.pause(500)

    집가고싶다 += 1

    if (집가고싶다 == 7) {
        집가고싶다 = 0
    }
})
