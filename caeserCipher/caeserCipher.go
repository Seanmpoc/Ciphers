package main

import (
	"fmt"
	"unicode"
)

func CaeserCipherEncode(text string, key int) string {
	var result string = ""

	for i := 0; i < len(text); i++ {
		char := rune(text[i])

		if unicode.IsUpper(rune(text[i])) {
			// Upper Case
			result += string(((char-'A')+rune(key)+26)%26 + 'A')
		} else if unicode.IsLower(rune(text[i])) {
			// Lower Case
			result += string(((char-'a')+rune(key)+26)%26 + 'a')
		} else {
			result += string(char)
		}
	}

	return result
}

func CaeserCipherDecode(text string, key int) string {
	var result string = ""

	for i := 0; i < len(text); i++ {
		char := rune(text[i])

		if unicode.IsUpper(rune(text[i])) {
			// Upper Case
			result += string(((char-'A')-rune(key)+26)%26 + 'A')
		} else if unicode.IsLower(rune(text[i])) {
			// Lower Case
			result += string(((char-'a')-rune(key)+26)%26 + 'a')
		} else {
			result += string(char)
		}
	}

	return result
}

func main() {
	var phrase string = "Hello, World!"
	var encryptedCaeserPhrase = "RQH YDULDWLRQ WR WKH VWDQGDUG FDHVDU FLSKHU LV ZKHQ WKH DOSKDEHW LV \"NHBHG\" EB XVLQJ D ZRUG. LQ WKH WUDGLWLRQDO YDULHWB, RQH FRXOG ZULWH WKH DOSKDEHW RQ WZR VWULSV DQG MXVW PDWFK XS WKH VWULSV DIWHU VOLGLQJ WKH ERWWRP VWULS WR WKH OHIW RU ULJKW. WR HQFRGH, BRX ZRXOG ILQG D OHWWHU LQ WKH WRS URZ DQG VXEVWLWXWH LW IRU WKH OHWWHU LQ WKH ERWWRP URZ. IRU D NHBHG YHUVLRQ, RQH ZRXOG QRW XVH D VWDQGDUG DOSKDEHW, EXW ZRXOG ILUVW ZULWH D ZRUG (RPLWWLQJ GXSOLFDWHG OHWWHUV) DQG WKHQ ZULWH WKH UHPDLQLQJ OHWWHUV RI WKH DOSKDEHW. IRU WKH HADPSOH EHORZ, L XVHG D NHB RI \"UXPNLQ.FRP\" DQG BRX ZLOO VHH WKDW WKH SHULRG LV UHPRYHG EHFDXVH LW LV QRW D OHWWHU. BRX ZLOO DOVR QRWLFH WKH VHFRQG \"P\" LV QRW LQFOXGHG EHFDXVH WKHUH ZDV DQ P DOUHDGB DQG BRX FDQ'W KDYH GXSOLFDWHV."
	var caeserKey int = 3

	var ceaserEncodeResult string = CaeserCipherEncode(phrase, caeserKey)
	var caeserDecodeResult string = CaeserCipherDecode(encryptedCaeserPhrase, caeserKey)

	fmt.Print("Word being encrypted: ", phrase)
	fmt.Print("\n\nShift key: ", caeserKey)
	fmt.Print("\nEncrypted Caeser Cipher Phrase: ", ceaserEncodeResult)
	fmt.Print("\nDecrypted Caeser Cipher Phrase: ", caeserDecodeResult)
}
