#include <stdio.h>
#include <stdlib.h>
struct frame
{
	int val;
	int rec;
};
void LRU(struct frame *frames, int no)
{
	int fault = 0, hit = 0;
	int i, inp = -1;
	int c = 0;
	do
	{
		int flag = 0;
		printf("Enter request (-1 to stop)\n");
		scanf("%d", &inp);
		if(inp == -1)
			break;
		for(i = 0; i < no; ++i)
		{
			if(frames[i].val == inp)
			{
				++hit;
				frames[i].rec = c;
				flag = 1;
				break;
			}
			else if(frames[i].val == -1)
			{
				++fault;
				frames[i].rec = c;
				frames[i].val = inp;
				flag = 1;
				break;
			}
		}
		if(flag == 0)
		{
			int LRU = 0;
			for(i = 0; i < no; ++i)
			{
				if(frames[i].rec < frames[LRU].rec)
					LRU = i;
			}
			frames[LRU].val = inp;
			frames[LRU].rec = c;
			++fault;
		}
		printf("Frames: ");
		for(i = 0; i < no; ++i)
		{
			if(frames[i].val == -1)
				break;
			printf("%d ", frames[i].val);
		}
		printf("\n");
		++c;
	}while(1);
	printf("Hit ratio: %f\n", (float)hit );
	printf("Miss ratio: %f\n", (float)fault );
	printf("Hit ratio: %f%\n", (float)hit * 100.0f/(float)(hit + fault));
	printf("Miss ratio: %f%\n", (float)fault * 100.0f/(float)(hit + fault));
	
}
int main()
{
	int no, i;
	printf("Enter number of frames\n");
	scanf("%d", &no);
	struct frame *frames = (struct frame *)malloc(sizeof(struct frame) * no);
	for(i = 0; i < no; ++i)
		frames[i].val = -1;
	LRU(frames, no);
	return 0;
}
