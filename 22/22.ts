import fs from 'fs'
import readline from 'readline'

class Day22 {
    mix(secret: bigint, val: bigint): bigint {
        return secret ^ val;
    }

    prune(secret: bigint): bigint {
        return secret % BigInt(16777216);
    }

// 15887950
// 16495136
// 527345
// 704524
// 1553684
// 12683156
// 11100544
// 12249484
// 7753432
// 5908254


// 1: 8685429
// 10: 4700978
// 100: 15273692
// 2024: 8667524

// 1: 8685429
// 10: 4700978
// 100: 15273692
// 2024: 8667524

// sum: 37327623

// 1
// 10
// 100
// 2024
    
    ithSecret(secret: bigint, iterations: number): bigint {
        for (const _ of Array.from({ length: iterations })) {
            const mul64 = secret * BigInt(64);
            secret = this.mix(secret, mul64);
            secret = this.prune(secret);
    
            const div32 = secret / BigInt(32);
            secret = this.mix(secret, div32);
            secret = this.prune(secret);
    
            const mul2048 = secret * BigInt(2048);
            secret = this.mix(secret, mul2048);
            secret = this.prune(secret);        
        }

        return secret
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

        // multiply secret by 64 -> mul_res
        // mul_res mix into secret
        // prune secret

        // divide secret by 32 -> div_res
        // div_res round down to nearest integer
        // div_res mix into secret
        // prune secret

        // multiply secret by 2048 -> mul2_res
        // mul2_res mix into secret
        // prune secret

        // mix: biwise xor
        // prune: % 16777216

        this.ithSecret(BigInt(123), 10)

        // name this better
        let pt_1_res = BigInt(0);
        for (const initialPrice of lines) {
            const r = this.ithSecret(BigInt(initialPrice), 2000)
            pt_1_res += r
        }
        console.log(`pt_1_res: ${pt_1_res}`)

        return ['TODO', 'TODO']
    }
}

const s = new Day22();
s.solve();