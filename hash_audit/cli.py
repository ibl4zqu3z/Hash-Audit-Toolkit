import argparse
from hash_audit.detector import identify_hash
from hash_audit.verifier import hash_text
from hash_audit.auditor import audit_hash_with_wordlist
from hash_audit.filehash import hash_file
from hash_audit.reporter import save_report

SUPPORTED_ALGOS = ["md5", "sha1", "sha224", "sha256", "sha384", "sha512"]

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Hash Audit Toolkit - análisis y auditoría controlada de hashes"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    identify_parser = subparsers.add_parser("identify", help="Identifica algoritmos probables")
    identify_parser.add_argument("hash_value", help="Hash a identificar")

    verify_parser = subparsers.add_parser("verify", help="Genera hash de un texto")
    verify_parser.add_argument("--text", required=True, help="Texto de entrada")
    verify_parser.add_argument("--algorithm", required=True, choices=SUPPORTED_ALGOS, help="Algoritmo hash")
    verify_parser.add_argument("--expected", help="Hash esperado para comparar")

    audit_parser = subparsers.add_parser("audit", help="Audita un hash con una wordlist autorizada")
    audit_parser.add_argument("--hash", dest="hash_value", required=True, help="Hash objetivo")
    audit_parser.add_argument("--wordlist", required=True, help="Ruta a la wordlist")
    audit_parser.add_argument("--algorithm", choices=SUPPORTED_ALGOS, help="Algoritmo si se conoce")
    audit_parser.add_argument("--report", help="Ruta para guardar informe JSON")

    filehash_parser = subparsers.add_parser("filehash", help="Calcula hash de un fichero")
    filehash_parser.add_argument("filepath", help="Ruta del fichero")
    filehash_parser.add_argument("--algorithm", default="sha256", choices=SUPPORTED_ALGOS, help="Algoritmo hash")

    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "identify":
        print(identify_hash(args.hash_value))

    elif args.command == "verify":
        generated = hash_text(args.text, args.algorithm)
        print(f"Algorithm : {args.algorithm}")
        print(f"Hash      : {generated}")
        if args.expected:
            print(f"Match     : {generated.lower() == args.expected.lower()}")

    elif args.command == "audit":
        result = audit_hash_with_wordlist(
            hash_value=args.hash_value,
            wordlist_path=args.wordlist,
            algorithm=args.algorithm
        )
        print(result["summary"])
        if args.report:
            save_report(result, args.report)
            print(f"Report saved to: {args.report}")

    elif args.command == "filehash":
        result = hash_file(args.filepath, args.algorithm)
        print(f"File      : {result['filepath']}")
        print(f"Size      : {result['size_bytes']} bytes")
        print(f"Algorithm : {result['algorithm']}")
        print(f"Hash      : {result['hash']}")
