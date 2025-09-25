-- SELECT
CREATE POLICY "select access policy for bucket example-knowledge-organisation-a"
ON storage.buckets FOR SELECT
USING (
	-- adjust restricted bucket name
    id = 'example-knowledge-organisation-a'
    -- adjust authorised users' IDs
    AND (select auth.uid()::text) IN (
        '455d3943-7a3f-4155-8761-90c4a3d25e4e',
        '5baa2288-120b-4010-b8a4-cb3fc32b8848' 
        )
);

-- INSERT
CREATE POLICY "insert access policy for bucket example-knowledge-organisation-a"
ON storage.buckets FOR INSERT
USING (
	-- adjust restricted bucket name
    id = 'example-knowledge-organisation-a'
    -- adjust authorised users' IDs
    AND (select auth.uid()::text) IN (
        '455d3943-7a3f-4155-8761-90c4a3d25e4e',
        '5baa2288-120b-4010-b8a4-cb3fc32b8848'
        )
);

-- UPDATE
CREATE POLICY "update access policy for bucket example-knowledge-organisation-a"
ON storage.buckets FOR UPDATE
USING (
	-- adjust restricted bucket name
    id = 'example-knowledge-organisation-a'
    -- adjust authorised users' IDs
    AND (select auth.uid()::text) IN (
        '455d3943-7a3f-4155-8761-90c4a3d25e4e',
        '5baa2288-120b-4010-b8a4-cb3fc32b8848'
        )
);

-- DELETE   
CREATE POLICY "delete access policy for bucket example-knowledge-organisation-a"
ON storage.buckets FOR DELETE
USING (
	-- adjust restricted bucket name
    id = 'example-knowledge-organisation-a'
    -- adjust authorised users' IDs
    AND (select auth.uid()::text) IN (
        '455d3943-7a3f-4155-8761-90c4a3d25e4e',
        '5baa2288-120b-4010-b8a4-cb3fc32b8848'
        )
);