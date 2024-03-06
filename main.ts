basic.showIcon(IconNames.Heart)
basic.pause(500)
huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_LINE_TRACKING)
basic.forever(function () {
    huskylens.request()
    if (huskylens.isAppear(1, HUSKYLENSResultType_t.HUSKYLENSResultBlock)) {
        basic.showIcon(IconNames.Happy)
        huskylens.writeOSD("Simos", 150, 30)
    } else {
        basic.showIcon(IconNames.Sad)
    }
    while (huskylens.isAppear_s(HUSKYLENSResultType_t.HUSKYLENSResultArrow)) {
    	
    }
    for (let index = 0; index < huskylens.readeArrow_index(1, 1, Content2.xOrigin); index++) {
    	
    }
})
