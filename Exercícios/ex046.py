from time import sleep
import emoji
print('{:-^55}'.format(' CONTAGEM REGRESSIVA '))
for c in range(10, -1, -1):
    print('>{}<'.format(c), end='  ')
    sleep(1)
print(emoji.emojize('\n          :sparkles::boom::sparkles:  EXPLOSION!  :sparkles::collision::sparkles:', use_aliases=True))
