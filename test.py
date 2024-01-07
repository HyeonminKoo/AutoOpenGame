import sys

# sys.argv[0]은 스크립트 파일의 경로이므로, 실제 인풋 파라미터는 sys.argv[1:]에서 시작합니다.
input_parameters = sys.argv[1:2]
input_parameters2 = sys.argv[2:3]

# 받은 인풋 파라미터 출력
print("Input Parameters:", input_parameters)
print("Input Parameters2:", input_parameters2)
input("Press Enter to exit...")

# 여기서부터 스크립트 로직을 계속 작성하면 됩니다.
