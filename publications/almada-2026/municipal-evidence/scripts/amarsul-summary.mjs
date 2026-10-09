import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

export const DEFAULT_CSV = fileURLToPath(new URL('../data/amarsul-2023-2024.csv', import.meta.url));

export function loadRows(path = DEFAULT_CSV) {
  const raw = readFileSync(path, 'utf8').trim().split(/\r?\n/);
  const expected = ['municipality','stream','year','tonnes','operator','source_edition'];
  if (raw.shift() !== expected.join(',')) throw new Error('Cabeçalho desconhecido — requer revisão manual');
  const rows = raw.map((line, i) => {
    const cells = line.split(',');
    if (cells.length !== 6) throw new Error('CSV inválido na linha ' + (i + 2));
    const [municipality,stream,yearString,tonnesString,operator,source_edition] = cells;
    const year = Number(yearString), tonnes = Number(tonnesString);
    if (![2023,2024].includes(year) || !Number.isInteger(tonnes) || tonnes < 0) throw new Error('Valor inválido na linha ' + (i + 2));
    return { municipality,stream,year,tonnes,operator,source_edition };
  });
  const seen = new Set();
  for (const r of rows) {
    const key = [r.municipality,r.stream,r.year].join(':');
    if (seen.has(key)) throw new Error('Duplicado: ' + key);
    seen.add(key);
  }
  return rows;
}
export function summary(rows) {
  const names = [...new Set(rows.map(r => r.municipality))].sort((a,b)=>a.localeCompare(b,'pt'));
  const get = (municipality,stream,year) => {
    const r=rows.find(x=>x.municipality===municipality&&x.stream===stream&&x.year===year);
    if (!r) throw new Error('Par município/indicador/ano em falta: '+municipality+' '+stream+' '+year);
    return r.tonnes;
  };
  return names.map(municipality => {
    const selective2023=get(municipality,'selective_packaging_paper_glass',2023);
    const selective2024=get(municipality,'selective_packaging_paper_glass',2024);
    const residual2023=get(municipality,'mixed_waste_treated',2023);
    const residual2024=get(municipality,'mixed_waste_treated',2024);
    const bio2023=get(municipality,'biowaste_treated',2023);
    const bio2024=get(municipality,'biowaste_treated',2024);
    const pct=(a,b)=>b===0?null:100*(a/b-1);
    // Indicador exploratório APENAS relativo às duas séries indicadas; NÃO é reciclagem.
    const twoStreamRatio=(s,r)=>100*s/(s+r);
    return {municipality,selective2023,selective2024,residual2023,residual2024,bio2023,bio2024,
      selectiveChangeT:selective2024-selective2023,
      residualChangeT:residual2024-residual2023,
      bioChangeT:bio2024-bio2023,
      selectiveChangePct:pct(selective2024,selective2023),
      residualChangePct:pct(residual2024,residual2023),
      twoStreamRatio2023:twoStreamRatio(selective2023,residual2023),
      twoStreamRatio2024:twoStreamRatio(selective2024,residual2024)};
  });
}
export function describe(rows) {
  const s=summary(rows),almada=s.find(r=>r.municipality==='Almada');
  return {n:s.length,selectiveUp:s.filter(r=>r.selectiveChangeT>0).length,
    residualUp:s.filter(r=>r.residualChangeT>0).length,
    bothUp:s.filter(r=>r.selectiveChangeT>0&&r.residualChangeT>0).length,
    almada};
}
if (process.argv[1] && fileURLToPath(import.meta.url) === process.argv[1]) {
  const d=describe(loadRows());
  console.log(JSON.stringify(d,null,2));
}
