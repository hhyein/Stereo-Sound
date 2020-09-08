------------------------------

<h2 align="center">mono to streo</h2>

<p align="center">
  to make a sound rotates like a circle
</p>

------------------------------

### 프로젝트 개요
1. 4초 오디오 샘플(16000Hz, 16bit, stereo)을 wave 파일로 준비한다.
2. 프로그램은 준비된 4초 오디오 샘플을 입력으로 읽어들인다.
3. 프로그램 출력은 원 모양으로 소리가 회전하는 효과를 나타내는 오디오 샘플 wave 파일로 저장된다.

------------------------------

### 원리
- 소리의 좌우 차이 구현을 위해 sin 함수 이용
- 소리의 앞뒤 차이 구현을 위해 cos 함수 이용

------------------------------

### [**자세한 내용**](https://github.com/hhyein/project-monotostreo/wiki)
