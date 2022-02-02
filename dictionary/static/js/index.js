
 if (performance.navigation.type == performance.navigation.TYPE_RELOAD){
    console.log("page loaded")

}
else
{
    console.info("page reloaded");
     let fl = document.getElementById("fl").value;
     let tl = document.getElementById("tl").value;
    if(fl != null && tl != null)
    {
        const ddl1 = document.getElementById("langf").options;
        const ddl2 = document.getElementById("langt").options;
        for(var i=0 ; i< ddl1.length; i++)
        {
            if(ddl1[i].value == fl)
            {
                document.getElementById("langf").options[i].selected = true; break;

            }
        }

        for(var i=0 ; i< ddl2.length; i++)
        {
            if(ddl2[i].value == tl)
            {
                document.getElementById("langt").options[i].selected = true;break;
            }
        }
    }

}
