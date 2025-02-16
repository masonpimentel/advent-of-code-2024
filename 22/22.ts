import fs from 'fs'
import readline from 'readline'

class Day22 {
    mix(secret: bigint, val: bigint): bigint {
        return secret ^ val;
    }

    prune(secret: bigint): bigint {
        return secret % BigInt(16777216);
    }

    generateNewSecret(secret: bigint): bigint {
        const mul64 = secret * BigInt(64);
        secret = this.mix(secret, mul64);
        secret = this.prune(secret);

        const div32 = secret / BigInt(32);
        secret = this.mix(secret, div32);
        secret = this.prune(secret);

        const mul2048 = secret * BigInt(2048);
        secret = this.mix(secret, mul2048);
        
        return this.prune(secret);
    }
    
    ithSecret(secret: bigint, iterations: number): bigint {
        for (const _ of Array.from({ length: iterations })) {
            secret = this.generateNewSecret(secret);
        }

        return secret
    }

    getPriceFromSecret(secret: bigint): number {
        return Number(secret % 10n);
    }

    getBananasFromBuyer(buyer: Record<string, number>, seq: string): number {
        if (seq in buyer) return buyer[seq];

        return 0;
    }

    sequencePrices(secret: bigint, iterations: number): Record<string, number> {
        const res: Record<string, number> = {};
        let curPrice = this.getPriceFromSecret(secret);
        let curSeq: number[] = [];
        
        // iterations - 1 because the original secret counts as one
        for (const _ of Array.from({ length: iterations - 1 })) {
            secret = this.generateNewSecret(secret);
            const newPrice = this.getPriceFromSecret(secret);
            // console.log(`secret ${secret} newPrice ${newPrice} curPrice ${curPrice}`)
            
            const thisDiff = newPrice - curPrice;

            curSeq.push(thisDiff);

            if (curSeq.length > 4) {
                curSeq.shift();
            }

            if (curSeq.length === 4) {
                const seqStr = curSeq.toString();

                if (!(seqStr in res)) {
                    res[seqStr] = newPrice;
                }
            }

            curPrice = newPrice;
        }

        return res;
    }

    async solve(): Promise<[string, string]> {
        const fileStream = fs.createReadStream('input.txt');

        const rl = readline.createInterface({
            input: fileStream,
            crlfDelay: Infinity
        });
    
        // name this better
        const lines: string[] = [];
        for await (const line of rl) { lines.push(line) };

        this.ithSecret(BigInt(123), 10)

        const buyers: Array<Record<string, number> > = [];

        // name this better
        let pt_1_res = BigInt(0);
        for (const initialPrice of lines) {
            const r = this.ithSecret(BigInt(initialPrice), 2000)
            pt_1_res += r
        }
        console.log(`pt_1_res: ${pt_1_res}`)

        const allSeqs: Set<string> = new Set();
        for (const initialPrice of lines) {
            const buyer = this.sequencePrices(BigInt(initialPrice), 2000);
            Object.keys(buyer).forEach((s) => allSeqs.add(s));
            buyers.push(buyer);
        }

        let pt_2_res = 0;
        let seqCount = 0;
        for (const seq of allSeqs) {
            let thisSeqRes = 0;
            for (const buyer of buyers) {
                thisSeqRes += this.getBananasFromBuyer(buyer, seq);
            }
          
            pt_2_res = Math.max(pt_2_res, thisSeqRes);
            seqCount++;
        }

        console.log(`pt_2_res: ${pt_2_res}`)


        return ['TODO', 'TODO']
    }
}

const s = new Day22();
s.solve();