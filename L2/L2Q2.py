

def solution(numbers):
    def version_key(version):
        parts = version.split('.')
        
        # Pad each part with leading zeros to ensure proper sorting
        padded_parts = [part.zfill(3) for part in parts]
        
        # Join the padded parts back into a version string
        padded_version = '.'.join(padded_parts)
        
        return padded_version
    
    sorted_numbers = sorted(numbers, key=version_key)
    
    return sorted_numbers
