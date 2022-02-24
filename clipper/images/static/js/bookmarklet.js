(function(){
    var jquery_version = '3.3.1';
    var site_url = 'http://127.0.0.1:8000/';
    var static_url = site_url + 'static/';
    var min_width = 100;
    var min_height = 100;

    function bookmarklet(msg) {
    // Здесь мы добавим код самого букмарклета.
    };
    // Проверка, подключена ли jQuery.
    if(typeofwindow.jQuery != 'undefined') {
        bookmarklet();
    } else {
            // Проверка, что атрибут $ окна не занят другим объектом.
            var conflict = typeof window.$ != 'undefined';
            // Создание тега <script> с загрузкой jQuery.
            var script = document.createElement('script');
            script.src = '//ajax.googleapis.com/ajax/libs/jquery/' +
            jquery_version + '/jquery.min.js';
            // Добавление тега в блок <head> документа.
            document.head.appendChild(script);
            // Добавление возможности использовать несколько попыток для загрузки jQuery.
            var attempts = 15;
            (function(){
            // Проверка, подключена ли jQuery
            if(typeof window.jQuery == 'undefined') {
            if(--attempts> 0) {
            // Если не подключена, пытаемся снова загрузить
            window.setTimeout(arguments.callee, 250)
            } else {
            // Превышено число попыток загрузки jQuery, выводим сообщение.
            alert('An error occurred while loading jQuery')
            }
            } else {
            bookmarklet();
            }
        })();
    }
})()