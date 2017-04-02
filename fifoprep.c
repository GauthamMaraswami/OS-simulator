#include<stdio.h>
int n,pg[30],fr[10];
void fifo()
{
int i,f,r,s,count,flag,num,psize,hit;
	f=0;
	r=0;
	s=0;
	flag=0;
	count=0;
	hit=0;
	printf("\nEnter size of page frame:");
	scanf("%d",&psize);
	for(i=0;i<psize;++i)
	{
		
		fr[i]=-1;	
	}
	while(s<n)	
	{
		printf("hi");
		flag=0;
		for(i=0;i<psize;++i)
			{
				if(pg[s]==fr[i])
				{
					flag=1;
					hit++;
					s++;
					printf("\nhit %d:",pg[s]);
					break;
				}
			}
		if(flag==0)
		{
			printf("\nmiss %d:",pg[s]);
			if(r<psize)
			{	
				fr[r]=pg[s];
				r++;
				s++;
				count++;
			}
			else
			{
				if(f<psize)
				{
					fr[f]=pg[s];
					s++;
					f++;
					count++;
				}
				else 
					{f=0;
					
					fr[f]=pg[s];
					s++;
					f++;
					count++;
				}
			}
		}
		printf("\n");
		printf(" %d\t",pg[s-1]);			
		for(i=0;i<psize;i++)
		{
			printf(" %d\t",fr[i]);
		}
	}
	printf("\nhit=%d",hit);
	printf("\nfault=%d",count);
	float hr=hit*1.0/n;
	printf("\nhitratio=%f",hr);
	float fr=count*1.0/n;
	printf("\nfault ratio=%f",fr);

}
void main()
{
int i,ch;
	printf("\nEnter total number of pages:");
	scanf("%d",&n);
	printf("\nEnter sequence:");
	for(i=0;i<n;i++)			//accepting sequence
		scanf("%d",&pg[i]);
	fifo();
}

