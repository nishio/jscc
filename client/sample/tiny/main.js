goog.provide("main.main");
main.main = function(){
    window.alert("hello!");
    var not_used;
    window.alert(not_usd); // typo
    /* it will cause:
    js/main.js:5: ERROR - variable not_usd is undeclared
    window.alert(not_usd); // typo
                 ^
     */
}