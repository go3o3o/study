// JetBrains 
// JAVA를 보완하기 위해 만든 언어
// https://kotlinlang.org 

fun main(args: Array<String>) {
    print("Hello World")
}
fun sum(a: Int, b: Int): Int {
    return a + b
}
fun sum(a: Int, b: int) = a + b

val a: Int = 1
val b = 2
val c = 3.14
val d: String
d = "필수로 있어야 하는 구문"
// d = "d의 초기값이 없으면 null이 될 수 있는데, d는 null이 될 수 없기 때문에"
val e: String?
val d: String = "첫번째 초기화"
e = "두번째 초기화"

var str String = "abcd"
str = "abcd" + 1 // abcd1
str = "abcd" + "efg" // abcdefg

val myTrue: Boolean = true
val myFalse: Boolean = false
val boolNull: Boolean? = null

// for 문
for (i in 1..5) {
    println(i) // 1 2 3 4 5
}
for (i in 6 downTo 0 step 2) {
    println(i) // 6 4 2 0
}
for (i in 1..5 step 3) {
    println(i) // 1 4
}
for (i in 1 until 10) {
    println(i) // 1 2 3 4 5 6 7 8 9
}
val numberList = listOf(100, 200, 300)
for (number in numberList) {
    println(number) // 100 200 300
}

// while 문
var x = 5
while (x > 0) {
    println(x) // 5 4 3 2 1
    x--
}
x = 0
while (x > 0) {
    prinln(x) // 출력 없음
    x--
}
var y = 0
do {
    print(y) // 0
    y--
} while (y > 0)

// if 문 
var max: Int
if (a > b) {
    max = a
} else {
    max = b
}
var max = if (a > b) {
    print("Choose a")
    a
} else {
    print("Choose b")
    b
}

// when 문 
when (x) {
    1 -> print("x == 1")
    2 -> print("x == 2")
    else -> {
        print("x is neither 1 nor 2")
    }
}
when (x) {
    0, 1 -> print("x == 0 or x == 1")
    else -> print("otherwise")
}
when (x) {
    in 1..10 -> print("x in [1~10]")
    !in 10..20 -> print("x not in [10~20]")
    else -> print("otherwise")
}
when (x) {
    is Int -> print("x type is Integer")
    else -> print("x type is not Integer")
}

//// JAVA vs Kotlin
// 1. Null Safe
// JAVA
Integer a = 100; 
a = null; 
a.sum(); // NullPoinstException 발생할 수 있음
if (a != null) a.sum(); 
// Kotlin
val b: Int? = 100
val c: Int = 100 
b?.sum() // null 일 경우 실행하지 않음 
c.sum() // nullsafe한 타입(절대로 null 이 될 수 없음을 암시)

// 2. Scope Function (apply, with, let, also, run)
// https://kotlinlang.org/docs/scope-functions.html#function-selection 
// JAVA
Person person = new Person();
person.firstName = "Fast";
person.lastName = "Compus";
// Kotlin - apply 함수를 사용하여 객체 내부에 있는 함수 초기화 가능
val person = Person().apply {
    firstName = "Fast"
    lastName = "Campus"
}

// JAVA
int value = Random().nextInt(100);
System.out.print(value);
// Kotlin - also 함수를 사용하여 객체 리턴 값을 파라미터로 받기 가능하기 때문에 유효성 검사 혹은 디버깅할 때 많이 사용함
Random.nextInt(100).also {
    print("getRandomInt() generated value $it")
}
Random.nextInt(100).also { value -> 
    print("getRandomInt() generated value $value")
}

// JAVA 
Integer number = null;
String sumNumberStr = null;
if (number != null) {
    sumNumberStr = "" + sum(10, number);
} else {
    sumNumberStr = "";
}
// Kotlin - let 함수
val number: Int?
val sumNumberStr = number?.let {
    "${sum(10, it)}"
}.orEmpty()

// JAVA 
Person person = new Person()
person.work();
person.sleep();
System.out.println(person.age);
// Kotlin - with 함수
val person = Person()
with (person) {
    work()
    sleep()
    println(age)
}

// JAVA 
service.port = 8080;
Result result = service.query();
// Kotlin - run 함수 (with 함수와 다르게 확장 가능성 있음)
val result = service.run {
    port = 8080
    query()
}

// 3. Data Class
// JAVA
public class JavaObject {
    private String s; 
    JavaObject(String s) {
        this.s = s;
    }
    public String getS() {
        return s;
    }
    public void setS(String s) {
         this.s = s;
    }
    // copy, toString, hashCode 등등 생략
}
// Kotlin
data class JavaObject(val s: String?)

// 4. Lambda expression 
// JAVA
button.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
    }
})
// Kotlin (it 으로도 접근 가능)
button.setOnClickListener { view -> 
}

// 5. lateinit, lazy init
// NullSafe 한 코드를 사용하기 위해선 non-null Type 으로 변수를 선언함 
// lateinit: 나중에 초기화 해줄게요~
var nullableNumber: Int? = null 
lateinit var lateinitNumber: Int
lateinitNumber = 10
nullableNumber?.add()
lateinitNumber.add()
// lazy init: 나중에 사용할때 값 할당해줄게요~ (사용하기 전에는 할당 X)
val lazyNumber: Int by lazy {
    100
}
lazyNumber.add() // 이 때 100 할당됨
