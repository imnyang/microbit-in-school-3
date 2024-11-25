let 집가고싶다 = 0
let 집안가고싶다 = -1
basic.forever(function on_forever() {
    
    
    basic.showArrow(집가고싶다)
    basic.clearScreen()
    basic.pause(500)
    집가고싶다 += 1
    if (집가고싶다 == 7) {
        집가고싶다 = 0
    } else {
        집안가고싶다 -= 1
    }
    
})
