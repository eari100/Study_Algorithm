public class ExMath {
    // 임의의 좌표가 원의 범위안에 포함되어있는지 체크
    private boolean checkInCircle(int R, int X, int TX, int Y, int TY) {

        // (반지름^2) > (((원의 중심 좌표 X - 임의의 좌표 TX) ^ 2) + ((원의 중심 좌표 Y - 임의의 좌표 TY) ^ 2)))
        if (Math.pow(R, 2) >= (Math.pow(X - TX, 2) + Math.pow(Y - TY, 2))) return true;

        return false;
    }
}
