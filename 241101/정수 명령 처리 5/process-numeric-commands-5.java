import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());

        List<Integer> list=new ArrayList<>();

        for(int i=0;i<n;i++){
            st=new StringTokenizer(br.readLine());
            String oper=st.nextToken();
            if(oper.equals("push_back")){
                int k=Integer.parseInt(st.nextToken());
                list.add(k);
            }else if(oper.equals("get")){
                int k=Integer.parseInt(st.nextToken());
                System.out.println(list.get(k-1));
            }else if(oper.equals("size")){
                System.out.println(list.size());
            }else if(oper.equals("pop_back")){
                list.remove(list.size()-1);
            }
        }
    }
}