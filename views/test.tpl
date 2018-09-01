<!DOCTYPE html>
<html lang="ja">

<head>
  <meta charset="utf-8">
  <meta name='keywords' content=''>
  <meta name='description' content="">
  <meta name='viewport' content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" media="screen" href="static/css/top.css">

  <!-- <link rel="stylesheet" media='screen and (min-width:0) and (max-width:375px)' href="static/css/top_sp.css">
  <link rel="stylesheet" media='screen and (min-width:376px) and (max-width:768px)' href="static/css/top_pad.css">
  <link rel="stylesheet" media='screen and (min-width:769px)' href="static/css/top.css"> -->

  <!-- <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script> -->




  <title>Heroku</title>

</head>

<body>
  <script>
    function statusChangeCallback(response) {
      console.log('statusChangeCallback');
      console.log(response);

      if (response.status === 'connected') {

        testAPI();
      } else if (response.status === 'not_authorized') {

        document.getElementById('status').innerHTML = 'Please log ' +
          'into this app.';
      } else {

        document.getElementById('status').innerHTML = 'Please log ' +
          'into Facebook.';
      }
    }

    function checkLoginState() {
      FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
      });
    }

    // function Logout() {
    //   FB.Logout(function(response) {
    //
    //   });
    // }

    window.fbAsyncInit = function() {
      FB.init({
        appId: '704097009951110',
        status : true,
        cookie: true,
        xfbml: true,
        version: 'v3.1'
      });

      FB.getLoginStatus(function(response) {
        statusChangeCallback(response);
      });

      // FB.Logout(function(response) {
      //
      // });

      FB.AppEvents.logPageView();

    };

    (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) {
        return;
      }
      js = d.createElement(s);
      js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

    function testAPI() {
      console.log('Welcome!  Fetching your information.... ');
      FB.api('/me', function(response) {
        console.log('Successful login for: ' + response.name);
        document.getElementById('status').innerHTML =
          'Thanks for logging in, ' + response.name + '!';
      });
    }
  </script>


  <form action="/test" method="post">
    <article>
      <label>Amount: ¥500</label>
    </article>

    <script src="https://checkout.stripe.com/v2/checkout.js" class="stripe-button" data-key="{{ key }}" data-locale="auto" data-amount="500 " data-name="test" data-currency="jpy" data-image="static/img/ninwanko.png" data-locale="ja"></script>
  </form>

  <fb:login-button autologoutlink="true" scope="public_profile,email" onlogin="checkLoginState();" onclick="FB.logout(function() { document.location.reload(); });">
  </fb:login-button>


  <div id="status">
  </div>


</body>

</html>
