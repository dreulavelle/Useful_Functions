def scrub_m3u(input_file, output_file, language):
    # Output file containing only 1080p or 720p streams
    # In your designated language.
    lst = []
    language = f'tvg-language="{language}"'
    with open(input_file, 'r+') as f:
        for line1, line2 in zip(f, f):
            line1 = line1.split('\n')[0]
            line2 = line2.split('\n')[0]
            if ('(1080p)' in line1) or ('(720p)' in line1) and (f'tvg-language="{language}"' in line1):
                lst.append(line1 + '\n' + line2 + '\n')
            else:
                pass
                
    with open(output_file, 'a') as w:
        w.writelines('#EXTM3U\n')
        w.writelines(lst)

# Example: 
# local file = public.m3u
# save file as = HD.m3u
# Language = English

# Languages can be:
# English
# Spanish
# Italian
# French
# German
# Russian
# etc.. etc..

scrub_m3u('public.m3u', 'HD.m3u', 'English')
