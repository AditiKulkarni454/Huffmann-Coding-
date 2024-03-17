from collections import defaultdict
import heapq

def HuffmanCoding(s):

	print("############# Huffman Coding #############")
	print()
	print("The Input String for HuffmanCoding :",s)
	print()
	
	mp = defaultdict(int)
	for i in s:
		mp[i] += 1

	chars = []
	freq = []

	for i in mp:
		chars.append(i)
		freq.append(mp[i])

	HuffmanCoding_with_Char_and_Freq(chars,freq)


def HuffmanCoding_with_Char_and_Freq(chars,freq):

	mp = defaultdict(int)
	for i in range(len(chars)):
		mp[chars[i]] = freq[i]

	print("Char Array : ",chars)
	print("Freq Array : ",freq)

	str_len = sum(freq)

	dict1 = defaultdict(str)

	h = []

	for i in range(len(freq)):
		heapq.heappush(h,[freq[i],chars[i]])


	while len(h) > 1:
		left = heapq.heappop(h)
		right = heapq.heappop(h)
		
		freq_left = left[0]	
		freq_right = right[0]

		chars_left = left[1]
		chars_right = right[1]

		for j in chars_left:
			dict1[j] = '0' + dict1[j]

		for j in chars_right:
			dict1[j] = '1' + dict1[j]

		new_freq = freq_left + freq_right
		new_chars = chars_left + chars_right

		heapq.heappush(h,[new_freq,new_chars])

	print()
	print("Huffman Coding Table for the String :")
	print()

	
	for i in dict1:
		print(i, "-->",dict1[i],"[",len(dict1[i]),"bits ]")

	print()
	old_bits = 8 * str_len
	print("No of Bits Required Before Huffman Coding : ",8," x ",str_len, " = ",old_bits,"bits")
	print()

	print("No of Bits Required After Huffman Coding : ")
	ans = 0
	for i in dict1:
		print("(",mp[i],"x",len(dict1[i]),") +",end = " ")
		ans = ans + (mp[i] * len(dict1[i]))
	print("=",ans,"bits")

	new_bits = ans

	print()

	print("The Compression using HuffmanCoding is",old_bits,"bits --> ",new_bits,"bits = ",old_bits - new_bits,"bits")
	print()
	perc = ((old_bits - new_bits) / old_bits) * 100 
	print("The Compression Percentage : ",round(perc,2),"% ")
	print()
	print("------------------------------------------------------------------------------------------------------------------")
	print("------------------------------------------------------------------------------------------------------------------")
	
	print()


#Main Function: 

#HuffmanCoding with Directly String as an Input
HuffmanCoding("ababshsshbadwdihddhwahihdhdh")


chars = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]

#HuffmanCoding with Character and Frequency Array
HuffmanCoding_with_Char_and_Freq(chars,freq)