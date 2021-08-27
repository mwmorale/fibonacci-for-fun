// Recursive Fibonacci sequence -> Java

// Function input should be an Integer

class Main {
  public static int fibFunc(int x) {
    if(x==0 || x==1){
      return x;
    }
    return fibFunc(x-1)+fibFunc(x-2);
  }
  public static void main(String[] args) {
    //System.out.println(fibFunc(8));
  }
  
}