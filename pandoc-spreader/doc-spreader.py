import os

selected_outputs = dict()
selected_outputs['html'] = 'html'
selected_outputs['docx'] = 'docx'
selected_outputs['beamer'] = 'tex'
selected_outputs['epub'] = 'epub'
selected_outputs['gfm'] = 'md'
selected_outputs['ipynb'] = 'ipynb'
selected_outputs['opml'] = 'opml'
selected_outputs['pptx'] = 'pptx'
selected_outputs['slideous'] = 'html'
selected_outputs['slidy'] = 'html'
selected_outputs['dzslides'] = 'html'
selected_outputs['revealjs'] = 'html'
selected_outputs['s5'] = 'html'

input_file = 'samplepaper.tex'
input_type = 'latex'
output_title = 'hcii2020'

for output_type in selected_outputs:
    os.system(f'pandoc {input_file} -f {input_type} -t {output_type} -s -o {output_title}_{output_type}.{selected_outputs[output_type]}')

