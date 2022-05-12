<?php
     if(isset($_GET['on'])){
             exec('/usr/bin/python creationMap.py');
     }

     else if(isset($_GET['off'])){
             exec('/usr/bin/python creationMap.py');
             header('Location: interfaceGraphique.html');
             exit();
     }

     else if(isset($_GET['reboot'])){
             echo "Reboot initiated...";
     }
?>