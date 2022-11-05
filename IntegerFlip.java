import java.util.HashMap;
import java.util.Map;

public class IntegerFlip{
    public IntegerFlip(int n ){
    
        StringBuilder sb = new StringBuilder();
        sb.append(1 / n );
        long remainder = 1 % n;
        sb.append(".");
        Map<Long, Integer> map = new HashMap<>();
        while (remainder != 0){
            map.put(remainder, sb.length());
            remainder *= 10;
            sb.append(remainder / n);
            remainder %= n;
            Integer index = map.get(remainder);
            if (index != null){
                String substring = sb.substring(index);
                sb.append(" ").append(substring);
                break;
            }
            if (remainder == 0 ){
                sb.append(0).append(" ").append(0);
            }
        }
        System.out.println(sb.toString());
    }
    public static void main(String[] args){
        IntegerFlip michael = new IntegerFlip(10);
    }
}