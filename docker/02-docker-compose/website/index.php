<html>
    <head>
        <title>My Shop</title>
    </head>

    <body>
        <h1>Welcome to my shop</h1>
        <ul>
            <?php

            $json = file_get_contents('http://product-service/');
            $obj = json_decode($json);

            $Users = $obj->Users;

            foreach ($Users as $user) {
                echo "<li>$user</li>";
            }

            ?>
        </ul>
    </body>
</html>
