---
layout: post
author: elliott
date: 2013-09-11 9:15am
---

This is how Ruby reads the posts for the first time:

```ruby

    # Read all the files in <source>/<dir>/_posts and create a new Post
    # object with each one.
    #
    # dir - The String relative path of the directory to read.
    #
    # Returns nothing.
    def read_posts(dir)
      entries = get_entries(dir, '_posts')

      # first pass processes, but does not yet render post content
      entries.each do |f|
        if Post.valid?(f)
          post = Post.new(self, self.source, dir, f)

          if post.published && (self.future || post.date <= self.time)
            aggregate_post_info(post)
          end
        end
      end
    end
```

See it [here](https://github.com/mojombo/jekyll/blob/master/lib/jekyll/site.rb#L150).


The `get_entries` function seems to be doing important work here.  Let's see what it does:

```ruby
    # Read the entries from a particular directory for processing
    #
    # dir - The String relative path of the directory to read
    # subfolder - The String directory to read
    #
    # Returns the list of entries to process
    def get_entries(dir, subfolder)
      base = File.join(self.source, dir, subfolder)
      return [] unless File.exists?(base)
      entries = Dir.chdir(base) { filter_entries(Dir['**/*']) }
      entries.delete_if { |e| File.directory?(File.join(base, e)) }
    end
```


Finally, look at the `posts` row below to see that the posts are sorted in reverse.  This isn't intuitive until you do a little research into [how Ruby sorts](http://stackoverflow.com/questions/2637419/understanding-ruby-array-sort).

```ruby

    def site_payload
      {"jekyll" => { "version" => Jekyll::VERSION },
       "site" => self.config.merge({
          "time" => self.time,
          "posts" => self.posts.sort { |a, b| b <=> a },
          "pages" => self.pages,
          "html_pages" => self.pages.reject { |page| !page.html? },
          "categories" => post_attr_hash('categories'),
          "tags" => post_attr_hash('tags')})}
    end
```

We can type `ls _posts` in Linux to see how those files will be listed.  Posts with the same date/time will be listed in file order.

Cool!
