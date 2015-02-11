#include <stdio.h>

int number(char simvol)
{
    int rezult;
    if ((simvol>=0x30)&&(simvol <=0x39)) rezult = simvol - 0x30;
    else rezult = -1;
    return rezult;
}
main()
{

    int rezult,rez_first = 0;
    char simvol ;
    printf ("\ninput simvol");
    while (simvol!='x')
    {
        simvol = getchar();
        if (simvol=='x')    printf("Exit from programm");
        else
        {
            if (simvol!=0x0A)
            {
                rezult = number(simvol);
                if (rezult>0)printf("rez int %d",rezult);
                else printf ("not int ");
                printf("\ninput simvol");
            }
        }
    }
}
