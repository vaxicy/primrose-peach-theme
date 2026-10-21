// Primrose Peach Theme — peach, primrose pink and mint
import { readFile } from 'node:fs/promises';

const GARDEN_PALETTE = {
  peach: '#FCD6B4',
  primrose: '#FFACBD',
  butter: '#FBF3C0',
  mint: '#D3F4F3',
  leaf: '#B1D29B',
};

export class GardenBed {
  constructor(name = 'Sunny border') {
    this.name = name;
    this.palette = GARDEN_PALETTE;
  }

  /** Blend two petals into a softer shade. */
  blend(from, to, ratio = 0.5) {
    const parse = (hex) =>
      [1, 3, 5].map((i) => parseInt(hex.slice(i, i + 2), 16));
    const [a, b] = [parse(from), parse(to)];
    const channel = (value, i) =>
      Math.round(value * (1 - ratio) + b[i] * ratio);
    const toHex = (value) => value.toString(16).padStart(2, '0');
    return '#' + a.map(channel).map(toHex).join('');
  }

  async readPlan(file) {
    const content = await readFile(file, 'utf8');
    const rows = content.split('\n').filter(Boolean);
    return {
      name: this.name,
      kinds: Object.keys(this.palette).length,
      rows: rows.length,
      content,
    };
  }
}

const bed = new GardenBed();
const shade = bed.blend(GARDEN_PALETTE.primrose, GARDEN_PALETTE.mint);

console.log(`border shade: ${shade}`);
