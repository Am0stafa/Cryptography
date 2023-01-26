# implementation of cryptographic algorithm

## Appendix

Cryptography aims to provide ongoing confidentiality, data integrity, and authenticity, even in the face of an attack. Confidentiality involves ensuring data privacy through the use of encryption. Data integrity deals with data consistency and detection of tampering and modification of data through the use of hashing. Authenticity ensures that the data comes from a trusted source by using public key cryptography

Encryption algorithms converts plaintext data into cipher text that conceals the original content. Plaintext data can be restored from the cipher text through decryption. Encryption can be **symmetric** (encryption/decryption with same secret-key) or **asymmetric** (encryption/decryption using a public and private key pair that are mathematically binded).

**Symmetric-key encryption algorithms:** use the same key for both encryption and decryption. This type of encryption is fast and suitable for bulk data processing. Since everybody who has access to the key is able to decrypt the encrypted content, this method requires careful key management and centralized control over key distribution.

```
               secret key
                   |
                   v
 plaintext ---> encrypt ---> ciphertext


               secret key
                   |
                   v
 plaintext <--- decrypt <--- ciphertext
```


**Public-key encryption algorithms:** operate with two separate keys: the public key and the private key. The public key can be distributed freely while the private key shouldn't be shared with anyone. A message encrypted with the public key can only be decrypted with the private key and vice-versa. Since asymmetric encryption is several times slower than symmetric operations, it's typically only used to encrypt small amounts of data, such as symmetric keys for bulk encryption.

![](https://raw.githubusercontent.com/nakov/Practical-Cryptography-for-Developers-Book/master/.gitbook/assets/asymmetric-encryption-diagram.png)


**Hashing** isn't a form of encryption, but it does use cryptography. Hash functions deterministically map arbitrary pieces of data into fixed-length values. It's easy to compute the hash from the input, but very difficult (i.e. infeasible) to determine the original input from the hash. Additionally, the hash will completely change when even a single bit of the input changes. Hash functions are used for integrity verification, but don't provide an authenticity guarantee.

**Message Authentication Codes:** (MACs) combine other cryptographic mechanisms (such as symmetric encryption or hashes) with secret keys to provide both integrity and authenticity protection. However, in order to verify a MAC, multiple entities have to share the same secret key and any of those entities can generate a valid MAC. HMACs, the most commonly used type of MAC, rely on hashing as the underlying cryptographic primitive. The full name of an HMAC algorithm usually includes the underlying hash function's type (for example, HMAC-SHA256 uses the SHA-256 hash function).

**Signatures** combine asymmetric cryptography (that is, using a public/private key pair) with hashing to provide integrity and authenticity by encrypting the hash of the message with the private key. However, unlike MACs, signatures also provide non-repudiation property as the private key should remain unique to the data signer.

**Key Derivation Functions:** (KDFs) derive secret keys from a secret value (such as a password) and are used to turn keys into other formats or to increase their length. KDFs are similar to hashing functions but have other uses as well (for example, they are used as components of multi-party key-agreement protocols). While both hashing functions and KDFs must be difficult to reverse, KDFs have the added requirement that the keys they produce must have a level of randomness.
