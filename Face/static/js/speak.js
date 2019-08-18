//语音播报测试
function speakText(str){
    //var request=  new URLRequest();
    var url = "http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text=" + encodeURI(str);        // baidu
    //var url = "http://translate.google.cn/translate_tts?ie=UTF-8&tl=zh-CN&total=1&idx=0&textlen=19&prev=input&q=" + encodeURI(str); // google
    //request.url = encodeURI(url);
    // request.contentType = "audio/mp3"; // for baidu
    //request.contentType = "audio/mpeg"; // for google

　　var n = new Audio(url);

　　 n.src = url;

　　 n.play();
    　　
　　 // $("...").play();
　　// var sound = new Sound(request);
　　// sound.play();
}
