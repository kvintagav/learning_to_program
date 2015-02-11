#include <stdio.h>
#include <stdbool.h>

#define IN true
#define OUT  false
#define MAXLINE 20
int power (int base , int deg);
int getline(char line[],int maxline);
void copy(char to[], char from[]);
void reverse(char s[]);
int getline(char s_line[] , int lim)
{
    int c,i;
    for(i=0; i<lim-1 &&(c=getchar())!=EOF && c!='\n'; i++)
        s_line[i] = c;
    if (c=='\n')
    {
        s_line[i]= c;
        ++i;
    }
    s_line[i]='\0';
    return i;

}
void reverse(char s[])
{
    int i=0,j=0;
    char buf;
    while (s[i]!='\0')
        ++i;
    i-=2;
    printf("%d\n",i+1);
    for ( j = 0; i>j ;--i, ++j )
    {
        buf=s[i];
        s[i]=s[j];
        s[j]=buf;
    }
    /*
    while(i>j)
    {
        buf=s[i];
        s[i]=s[j];
        s[j]=buf;
        ++j;
        --i;
    }
    */
}
void copy (char to[],char from[])
{
    int  i= 0;
    while ((to[i] = from[i]) !='\0')
        ++i;

}
int power (int base, int deg)
{
    int rezult;
    for (rezult = 1; deg>0 ; --deg)
    {
        rezult=rezult*base;
    }
    return rezult ;

}

main()
{
   /* float fahr, celsium;
    int lower, upper, step;
    lower = 0;
    upper = 300;
    step = 10;

    fahr =lower;

    while (fahr <=upper)
    {
        celsium = (5.0/9.0)*(fahr-32.0);
        printf("fahr = %3.0f ;celsium = %6.2f\n",fahr,celsium);
        fahr = fahr + step;
    }
    */
    /*
    int fahr;
    for (fahr = 0 ; fahr<=300 ; fahr+=10)
    {
        printf("fahr = %3d ; cell = %6.2f\n", fahr,(5.0/9.0)*(fahr-32.0));
    }
    */
    /*
    int c;
    c = getchar();

    while (c !=EOF){
    //EOF - символ конца файла, не поместитсяв char, поэтому берем int
        putchar(c);
        c = getchar();

    }
    */
    /*
    int c ;
    while ((c=getchar())!=EOF)
        putchar(c);
    */
    /*
    int index;
    for (index = 0 ; index<=10 ; ++index)
        printf("%d\n",index);
    */
    /*
    int c ,mount_lit = 0,mount_word = 0,mount_string = 0;
    bool state = OUT;

    while ((c=getchar())!=EOF)
    {


        ++mount_lit;
        if (c=='\n')
            ++mount_string;
        if (c== ' ' || c == 'n' || c == '\t')
            state = OUT;
        else if (state ==OUT){
            state =IN;
            ++mount_word;
        }
        putchar(c);
    }
    printf("exit ,%d,%d,%d",mount_lit,mount_word,mount_string);
    */
    /*
    int numb, step,fall;
    bool ok = true;
    printf("input number: ");
    numb = getchar();
    numb -= 0x30;
    fall = getchar();
    printf("number was input: %d\n",numb);
    printf("input degree: ");
    step = getchar();
    step -= 0x30;
    printf("input degree%d\n",step);

    printf("rezult power:%d",power(numb,step));
    */

    int len;
    int max = 0;
    char line[MAXLINE];
    char longest[MAXLINE];
/*
    while ((len = getline(line,MAXLINE))>1)
    if (len >max){
        max =len;
        copy (longest,line);
        printf("len = %d,max=%d\n",len,max);
    }
    if (max > 0)
        printf("%s\n max=%d" ,longest,max);
*/
/*
    len = getline(line,MAXLINE);
    reverse(line);
    printf("%s\n",line);
*/


    return 0;
}
