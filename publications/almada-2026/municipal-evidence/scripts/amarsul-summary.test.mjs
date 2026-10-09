import test from 'node:test';
import assert from 'node:assert/strict';
import { loadRows, summary, describe } from './amarsul-summary.mjs';
test('completude e unicidade: 9 municípios x 3 fluxos x 2 anos', () => {
  const rows=loadRows();assert.equal(rows.length,54);assert.equal(new Set(rows.map(r=>r.municipality)).size,9);
});
test('séries Almada coincidem com fonte do operador', ()=>{
  const a=summary(loadRows()).find(x=>x.municipality==='Almada');
  assert.equal(a.selective2023,10757);assert.equal(a.selective2024,12838);
  assert.equal(a.residual2023,66267);assert.equal(a.residual2024,68920);
  assert.equal(a.bio2023,4068);assert.equal(a.bio2024,4682);
  assert.equal(a.selectiveChangeT,2081);assert.equal(a.residualChangeT,2653);
  assert.ok(Math.abs(a.selectiveChangePct-19.346)<0.001);
  assert.ok(Math.abs(a.twoStreamRatio2024-a.twoStreamRatio2023-1.736662)<0.005);
});
test('crescimento conjunto em oito dos nove municípios', ()=>{
  const d=describe(loadRows());assert.equal(d.selectiveUp,9);assert.equal(d.residualUp,8);assert.equal(d.bothUp,8);
});
