#include<stdio.h>
int n,pg[30],fr[10];
void optimal()
{
	int count[10],i,j,r,fault,f,flag,temp,current,c,dist,max,m,cnt,p,x;
	fault=0;
	dist=0;
	r=0;
	int hit=0;
	printf("\nEnter frame size:");
	scanf("%d",&f);
	for(i=0;i<f;i++)
	{
		count[i]=0;
		fr[i]=-1;
	}
	for(i=0;i<n;++i)
	{
		flag=0;
		for(j=0;j<f;++j)
		{
			if(pg[i]==fr[j])
			{
			hit++;
			flag=1;
			printf("\nhit %d: ",pg[i]);
			break;
			}
		}
		if(flag==0&&r<f)
		{
			printf("\nmiss %d:",pg[i]);
			fr[r]=pg[i];
			r++;
			fault++;
		
		}
		else if(flag==0&&r==f)
		{
			fault++;
			printf("\nmiss %d:",pg[i]);
			for(cnt=0;cnt<f;++cnt)
			{
				current=fr[cnt];
				for(c=i;c<n;c++)
				{
					if(current!=pg[c])
						count[cnt]++;
					else
						break;
				}
			
			}
			max=0;
			for(m=0;m<f;m++)
			{
				if(count[m]>max)
				{
					max=count[m];
					p=m;
				}
			}
			fr[p]=pg[i];
		
		}
		printf("\n %d\t",pg[i]);			
		for(x=0;x<f;x++)
		{
			printf("%d\t",fr[x]);
		}
	
	}
	printf("\nhit=%d",hit);
	printf("\nfault=%d",fault);
	float hr=hit*1.0/n;
	printf("\nhitratio=%f",hr);
	float fr=fault*1.0/n;
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
	optimal();
}

