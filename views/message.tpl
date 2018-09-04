<!DOCTYPE html>
<html lang="ja">

<head>
  <meta http-equiv="Content-Type" content="text/plain"; charset="UTF-8"; Content-Transfer-Encoding="base64" />
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/top.css">

  <!-- <link rel="stylesheet" media='screen and (min-width:0) and (max-width:375px)' href="static/css/top_sp.css">
  <link rel="stylesheet" media='screen and (min-width:376px) and (max-width:768px)' href="static/css/top_pad.css">
  <link rel="stylesheet" media='screen and (min-width:769px)' href="static/css/top.css"> -->

  <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
  <script type="text/javascript" src="static/js/test.js"></script>

  <title>Heroku</title>

</head>
<body>
  <div class='test'>
    <div class='img'>
      <p class='img_sub'><img src="static/img/ninwanko.png" alt=""></p>
    </div>
    <p class='test_sub'>{{message}}</p>
    <div class='text'>
      <p class='test_sub'>{{main}}</p>
      <div id='comment'>
        <form id='form' action="/text" method='POST'>
          <input id='test' type="text" name='form' maxlength="10" placeholder='入力してください。'>
          <input class="button" type="submit" value='テスト' />
        </form>
      </div>
    </div>
  </div>
</body>

</html>
