"""Direct reproduction of quartet sample means, OLS and correlations (no dependencies)."""
import argparse,csv,json,math
from pathlib import Path
from xml.sax.saxutils import escape

def stats(x,y):
    n=len(x)
    if n<3 or len(y)!=n:raise ValueError('at least 3 paired points required')
    if any(not math.isfinite(v) for v in x+y):raise ValueError('nonfinite data')
    mx=sum(x)/n;my=sum(y)/n
    xx=sum((v-mx)**2 for v in x);yy=sum((v-my)**2 for v in y)
    xy=sum((a-mx)*(b-my) for a,b in zip(x,y))
    if xx==0 or yy==0:raise ValueError('zero-variance predictor or outcome')
    slope=xy/xx;intercept=my-slope*mx
    return {'n':n,'mean_x':mx,'mean_y':my,'slope':slope,'intercept':intercept,'r_squared':xy*xy/(xx*yy)}

def load(path):
    with path.open(newline='',encoding='utf8') as f:
        reader=csv.DictReader(f)
        expected=[v+str(i) for i in range(1,5) for v in ('x','y')]
        if reader.fieldnames!=expected:raise ValueError('expected columns '+','.join(expected))
        data=list(reader)
    if not data:raise ValueError('empty data')
    return {str(i):([float(row['x'+str(i)]) for row in data],[float(row['y'+str(i)]) for row in data]) for i in range(1,5)}

def svg(data,results):
    # Identical axis limits intentionally show different point structures.
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="920" height="630" viewBox="0 0 920 630">','<rect width="920" height="630" fill="white"/>','<text x="460" y="30" font-size="22" text-anchor="middle">Anscombe’s quartet — published data</text>']
    for index,(name,(x,y)) in enumerate(data.items()):
        left=65+(index%2)*455;top=65+(index//2)*290
        X=lambda v:left+(v-3)/17*340
        Y=lambda v:top+225-(v-3)/11*225
        parts.extend([f'<text x="{left}" y="{top-13}" font-size="16">Dataset {escape(name)}</text>',f'<path d="M{X(3)} {Y(3)}V{Y(14)} M{X(3)} {Y(3)}H{X(20)}" stroke="black" fill="none"/>'])
        for xx,yy in zip(x,y):parts.append(f'<circle cx="{X(xx):.2f}" cy="{Y(yy):.2f}" r="4.5" fill="#2962a8"/>')
        fit=results[name];y1=fit['intercept']+fit['slope']*3;y2=fit['intercept']+fit['slope']*20
        parts.append(f'<line x1="{X(3)}" y1="{Y(y1):.2f}" x2="{X(20)}" y2="{Y(y2):.2f}" stroke="#b1442d" stroke-width="2"/>')
    return '\n'.join(parts+['</svg>'])+'\n'

def reproduce(path):
    data=load(path);results={k:stats(*v) for k,v in data.items()}
    return data,results

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('data',type=Path);ap.add_argument('--svg',type=Path);a=ap.parse_args()
    data,out=reproduce(a.data)
    print(json.dumps(out,indent=2))
    if a.svg:
        a.svg.parent.mkdir(parents=True,exist_ok=True);a.svg.write_text(svg(data,out),encoding='utf8');print('Wrote',a.svg)
if __name__=='__main__':main()
