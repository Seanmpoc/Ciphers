package main

import (
	"fmt"
	"unicode"
)

func createVigenereKeyword(phrase, key string) string {
	x := len(phrase)
	newKey := ""

	for i := 0; i < x; i++ {
		newKey += string(key[i%len(key)])
	}

	return newKey
}

func VigenereCipherEncode(text string, key string) string {
	result := ""

	for i, ch := range text {
		k := unicode.ToUpper(rune(key[i])) // key character
		shift := int(k - 'A')

		if unicode.IsLetter(ch) {
			base := 'A'
			if unicode.IsLower(ch) {
				base = 'a'
			}
			encoded := (int(ch-base) + shift) % 26
			result += string(rune(encoded) + base)
		} else {
			result += string(ch)
		}
	}

	return result
}

func vigenereCipherDecode(text string, key string) string {
	newKey := createVigenereKeyword(text, key) // repeat key to phrase length
	result := ""

	for i, ch := range text {
		k := unicode.ToUpper(rune(newKey[i])) // key character
		shift := int(k - 'A')

		if unicode.IsLetter(ch) {
			base := 'A'
			if unicode.IsLower(ch) {
				base = 'a'
			}
			// ensure positive before mod 26
			decoded := (int(ch-base) - shift + 26) % 26
			result += string(rune(decoded) + base)
		} else {
			result += string(ch)
		}
	}

	return result
}

func main() {
	var phrase string = "explanation"
	var vigenereKey string = "leg"

	var vigenereKeyword string = createVigenereKeyword(phrase, vigenereKey)
	var vigenereEncodeResult string = VigenereCipherEncode(phrase, vigenereKeyword)
	var vigenereDecodeResult string = vigenereCipherDecode(vigenereEncodeResult, vigenereKeyword)

	fmt.Print("Word being encrypted: ", phrase)
	fmt.Print("\n\nKey for Vigenere Cipher: ", vigenereKey)
	fmt.Print("\nKeyword created for Vigenere Cipher: ", vigenereKeyword)
	fmt.Print("\nEncrypted Vigenere Cipher Phrase: ", vigenereEncodeResult)
	fmt.Print("\nDecrypted Vigenere Cipher Phrase: ", vigenereDecodeResult)
}
