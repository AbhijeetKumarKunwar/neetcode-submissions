class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb=new StringBuilder();
        for(String s:strs){
            sb.append(s.length()+"#"+s);
        }
        System.out.println(sb.toString());
        return sb.toString();

    }

    public List<String> decode(String str) {
        List<String> res=new ArrayList<>();
        int i=0;
        while(i<str.length())
        {
           int deli=str.indexOf('#',i);
           int len=Integer.parseInt(str.substring(i,deli));
           res.add(str.substring(deli+1,len+deli+1));
           i=len+deli+1;

        }
        return res;

    }
}
