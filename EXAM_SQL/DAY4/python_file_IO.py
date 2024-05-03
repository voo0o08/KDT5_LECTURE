filename1 = input("원본파일이름을입력하시오:	")
filename2 = input("복사파일이름을입력하시오:	")

infile	= open(filename1, "rb")
outfile	= open(filename2, "wb")

# 입력파일에서1024	바이트씩읽어서출력파일에쓴다.
# 파일의마지막부분에서는읽어들인바이트수만큼파일에저장
while True:
     copy_buffer = infile.read(1024)
     print(len(copy_buffer))	#	실제읽어온바이트수출력
     if	not	copy_buffer:					#	파일의끝인경우,	empty	byte를리턴
         break
     outfile.write(copy_buffer)

infile.close()
outfile.close()
print(filename1+"를" + filename2 +"로복사하였습니다.")
# 정해진 만큼의 바이트를 읽어오다가 모자라면 그냥 남은 것만 읽어옴