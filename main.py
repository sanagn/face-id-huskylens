basic.show_icon(IconNames.HEART)
basic.pause(500)
huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_LINE_TRACKING)

def on_forever():
    huskylens.request()
    if huskylens.is_appear(1, HUSKYLENSResultType_t.HUSKYLENS_RESULT_BLOCK):
        basic.show_icon(IconNames.HAPPY)
        huskylens.write_osd("Simos", 150, 30)
    else:
        basic.show_icon(IconNames.SAD)
    while huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENS_RESULT_ARROW):
        pass
    for index in range(huskylens.readeArrow_index(1, 1, Content2.X_ORIGIN)):
        pass
basic.forever(on_forever)
