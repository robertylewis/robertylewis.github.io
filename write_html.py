import yaml
import os
import os.path

root = 'logic_and_modeling_2021/lectures'

with open('lecture_vids.yaml') as file:
    dict = yaml.load(file, Loader=yaml.FullLoader)

def write_header(file, title):
    file.write('<html>\n')
    file.write(f'<head><title>{title}</title></head>\n')
    file.write('<body>\n')

def write_footer(file):
    file.write('</body></html>')


def write_index():
    with open(f'{root}/index.html', 'w') as file:
        write_header(file, 'Logic and Modeling 2021: Lectures')
        file.write('<h1>Logic and Modeling 2021: Lectures</h1>\n')
        file.write('<ul>\n')
        for lec in dict:
            file.write(f'<li>Lecture {lec}</li>\n')
            file.write(f'  <ul>\n  <li><a href="lecture_{lec}/all.html">All videos</a></li>\n')
            for vid in dict[lec]:
                file.write(f'  <li><a href="lecture_{lec}/{vid}.html">Video {vid}: {dict[lec][vid]["title"]}</a></li>\n')
            file.write('  </ul>\n\n')
        file.write('</ul>')
        write_footer(file)

# returns a string
def write_video(num, title, entry_id, wid):
    return f"""
<h2>Video {num}: {title}</h2>
<iframe id="kaltura_player" src="https://cdnapisec.kaltura.com/p/1197662/sp/119766200/embedIframeJs/uiconf_id/38520132/partner_id/1197662?iframeembed=true&playerId=kaltura_player&entry_id={entry_id}&flashvars[streamerType]=auto&amp;flashvars[localizationCode]=en&amp;flashvars[leadWithHTML5]=true&amp;flashvars[sideBarContainer.plugin]=true&amp;flashvars[sideBarContainer.position]=left&amp;flashvars[sideBarContainer.clickToClose]=true&amp;flashvars[chapters.plugin]=true&amp;flashvars[chapters.layout]=vertical&amp;flashvars[chapters.thumbnailRotator]=false&amp;flashvars[streamSelector.plugin]=true&amp;flashvars[EmbedPlayer.SpinnerTarget]=videoHolder&amp;flashvars[dualScreen.plugin]=true&amp;flashvars[Kaltura.addCrossoriginToIframe]=true&amp;&wid={wid}" width="608" height="402" allowfullscreen webkitallowfullscreen mozAllowFullScreen allow="autoplay *; fullscreen *; encrypted-media *" sandbox="allow-forms allow-same-origin allow-scripts allow-top-navigation allow-pointer-lock allow-popups allow-modals allow-orientation-lock allow-popups-to-escape-sandbox allow-presentation allow-top-navigation-by-user-activation" frameborder="0" title="Kaltura Player"></iframe>
"""

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def write_lecture(lec):
    vids = dict[lec]
    try:
        os.makedirs(f'{root}/lecture_{lec}')
    except OSError as exc:
        pass
    with open(f'{root}/lecture_{lec}/all.html', 'w') as all_file:
        write_header(all_file, f'Logic and Modeling 2021: Lecture {lec}')
        all_file.write(f'<h1><a href="../index.html">Logic and Modeling 2021</a>: Lecture {lec}</h1>\n\n')
        for num in vids:
            vid_str = write_video(num, vids[num]['title'], vids[num]['entry_id'], vids[num]['wid'])
            all_file.write(vid_str + "\n\n")
            with open(f'{root}/lecture_{lec}/{num}.html', 'w') as single_file:
                write_header(single_file, f'Logic and Modeling 2021: Lecture {lec} video {num}')
                single_file.write(f'<h1><a href="../index.html">Logic and Modeling 2021</a>: Lecture {lec}</h1>\n\n')
                prev = str(int(num)-1)
                if prev in vids:
                    single_file.write(f'<h2><a href="{prev}.html">Video {prev}: {vids[prev]["title"]}</a></h2>\n\n')
                single_file.write(vid_str + "\n\n")
                next = str(int(num)+1)
                if next in vids:
                    single_file.write(f'<h2><a href="{next}.html">Video {next}: {vids[next]["title"]}</a></h2>\n\n')
                write_footer(single_file)
        write_footer(all_file)

write_index()

for lec in dict:
    write_lecture(lec)